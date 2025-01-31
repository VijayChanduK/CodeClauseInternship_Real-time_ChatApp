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
1. *Clone the repository*:
   ```bash
   git clone https://github.com/VijayChanduK/CodeClauseInternship_Real-time_ChatApp.git
   cd RealTimeChat
Install dependencies:

bash
Copy
pip install -r requirements.txt
Initialize the database:

bash
Copy
flask shell
>>> db.create_all()
>>> exit()
Run the application:

bash
Copy
python app.py
Open http://localhost:5000 in your browser.

Usage 🖥
Register: Create an account via /register.

Login: Use your credentials at /login.

Chat: Send messages in real-time.

Rooms: Default room is general (custom rooms can be added).

Logout: Click the logout link in the chat interface.

Demo 🎥
Chat Demo (Replace with your demo GIF)


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

Contributing 🤝
Fork the repository.

Create a branch: git checkout -b feature/your-feature.

Commit changes: git commit -m "Add your feature".

Push to the branch: git push origin feature/your-feature.

Open a pull request.
