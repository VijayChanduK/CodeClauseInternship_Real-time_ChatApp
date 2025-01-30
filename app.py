from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///chat.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize extensions
db = SQLAlchemy(app)
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    room = db.Column(db.String(50))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route("/")
@login_required
def home():
    return render_template("index.html", username=current_user.username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# WebSocket Handlers
@socketio.on("join")
def handle_join(data):
    room = data["room"]
    join_room(room)
    emit("message", {"msg": f"{current_user.username} joined {room}"}, room=room)

@socketio.on("message")
def handle_message(data):
    room = data["room"]
    message = Message(content=data["msg"], user_id=current_user.id, room=room)
    db.session.add(message)
    db.session.commit()
    emit("message", {"msg": f"{current_user.username}: {data['msg']}"}, room=room)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)