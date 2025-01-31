# Real-Time Chat Application 🚀

A real-time chat application built with *Flask, **WebSocket, and **SQLite*. Features user authentication, chat rooms, and message history.

---

## Features ✨
- *Real-Time Messaging*: WebSocket-based communication.
- *User Authentication*: Secure registration/login with password hashing.
- *Chat Rooms*: Join/create rooms (default: general).
- *Message History*: Messages persist in the database.
- *Responsive UI*: Clean and modern design.
- *Online Presence*: Track active users in the chat room.

---

## Technologies 🛠
- *Backend*: Python, Flask, Flask-SocketIO, Flask-SQLAlchemy
- *Frontend*: HTML/CSS, Vanilla JavaScript, Socket.IO Client
- *Database*: SQLite (easy migration to PostgreSQL/MySQL)
- *Tools*: Git, Pipenv (dependency management)

---

## Installation 📦

### Prerequisites
- Python 3.10+
- pip



### Steps  

1. **Clone the repository**:  
   Run the following command:  
   git clone https://github.com/yourusername/RealTimeChat.git  
   Then navigate to the project directory:  
   cd RealTimeChat  

2. **Install dependencies**:  
   Run the following command:  
   pip install -r requirements.txt  

3. **Initialize the database**:  
   Run the following commands one by one:  
   flask shell  
   >>> db.create_all()  
   >>> exit()  

4. **Run the application**:  
   Run the following command:  
   python app.py  

5. **Open the application**:  
   Open [http://localhost:5000](http://localhost:5000) in your browser.  



## Usage 🖥

1. **Register**:  
   - Create an account via `/register`.

2. **Login**:  
   - Use your credentials at `/login`.

3. **Chat**:  
   - Send messages in real-time.

4. **Rooms**:  
   - The default room is `general` (custom rooms can be added).

5. **Logout**:  
   - Click the logout link in the chat interface.


## Demo 🎥

**Chat Demo**

![Image](https://github.com/user-attachments/assets/6b675544-82bd-4825-be4c-777bf0110ea3)


## Folder Structure 📂  
```  
Copy RealTimeChat/  
├── app.py  
├── requirements.txt  
├── instance/  
│   └── chat.db  
├── static/  
│   ├── script.js  
│   └── styles.css  
└── templates/  
    ├── index.html  
    ├── login.html  
    └── register.html  
```  
