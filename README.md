# Flask Note-Taking App

A secure and efficient Note-Taking Web Application built with **Python (Flask)**. This project demonstrates a full-stack implementation featuring user authentication, database management with SQLAlchemy, and user-specific data isolation.

## Key Features

- **Secure Authentication:** Complete Sign Up & Log In system with password hashing (SHA256) and unique email validation.
- **Relational Database:** Utilizes **SQLite** & **SQLAlchemy (ORM)** to manage a One-to-Many relationship between Users and Notes.
- **Data Privacy:** Implements User Data Isolation, ensuring users can only access and manage their own notes.
- **Dynamic UI:** Responsive interface powered by **Bootstrap 4**, featuring real-time flash messages for user feedback (Success/Error).
- **Note Management:** Add and delete notes instantly with asynchronous JavaScript (Fetch API).

## Tech Stack
 - Python (Flask), SQLAlchemy, SQLite, HTML, CSS, JavaScript

## Project Structure
```Plaintext
flask-note-app/
├── website/                # Main application package
│   ├── static/             # Asynchronous Request Handler
│   ├── templates/          # HTML Templates
│   ├── __init__.py         # App factory & DB initialization
│   ├── auth.py             # Authentication routes (Login/Signup)
│   ├── models.py           # Database models (User, Note)
│   └── views.py            # Main application routes
├── instance/               # Database storage (Auto-generated)
└── main.py                 # Entry point
``` 

## How to Run

### 1. **Clone the repository**
```bash
git clone https://github.com/LittleCat1041/flask-note-app.git
```
### 2. **Install Dependencies**
```bash
cd flask-note-app
```
```bash
pip install -r requirements.txt
```
### 3. **Start the Application**
```bash
python main.py
```
### 4. **Open in Browser**
- The app will start running at `http://localhost:5000`

## Screenshot

<img width="1207" height="673" alt="image" src="https://github.com/user-attachments/assets/5f8c1240-cec9-4172-bfc8-ac3021db39bf" />

<img width="1207" height="680" alt="image" src="https://github.com/user-attachments/assets/3b6812a3-d86e-4c4c-8aa2-6d3776b06267" />

<img width="1212" height="677" alt="image" src="https://github.com/user-attachments/assets/9253617f-c68f-4408-ba5d-bd4b9eb95ed6" />

## Project Context
This project was developed to demonstrate proficiency in Backend Development using Python and Flask, focusing on MVC architecture and secure data handling.
