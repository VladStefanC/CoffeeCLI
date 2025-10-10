# ☕ CoffeeCLI

**CoffeeCLI** is a full-stack coffee recipe platform with a twist — it looks and feels like a **terminal interface**.  
Instead of clicking buttons, users type commands (like in a CLI) to browse coffee recipes, manage favorites, and more.

Built with a modern stack — **FastAPI**, **PostgreSQL**, and **React + Tailwind CSS 4** — CoffeeCLI combines the power of a traditional web app with the aesthetic of a command-line tool.

---

## 🖥️ Interface Concept

CoffeeCLI’s frontend mimics a **terminal window**, allowing users to interact using typed commands such as:

login
list recipes
show recipe espresso
favorite add cappuccino
logout

This design makes exploring and brewing digital coffee recipes feel fun and hacker-style, all while keeping a minimal and responsive layout.

---

## 🚀 Features

### Backend (FastAPI)
- **User authentication** powered by [FastAPI Users](https://frankie567.github.io/fastapi-users/)
- **PostgreSQL** database for:
  - User accounts
  - Coffee recipes
  - Favorite recipes per user
- Fully functional and tested through **Swagger UI** (`/docs`)
- Clean modular architecture (models, routes, schemas, etc.)

### Frontend (React + Tailwind CSS 4)
- **Terminal-style UI** — command-based navigation and actions
- **Authentication system** (Register, Login, Logout)
- Displays all recipes retrieved from the backend
- Future updates:
  - Show step-by-step brewing instructions
  - Display user favorites dynamically
  - Enhanced command set and syntax feedback

---

## 🧩 Tech Stack

| Layer | Technology |
|:------|:------------|
| Backend | [FastAPI]|
| Authentication | [FastAPI Users] |
| Database | PostgreSQL |
| Frontend | React + Tailwind CSS 4 |
| API Docs | Swagger UI |
| Interface | Custom terminal-style command parser |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/VladStefanC/CoffeeCLI.git
cd CoffeeCLI

```
### 2. Backend Setup

Create & Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```
Install requirements 
```bash
pip install -r requirments.txt
```

Create .env file in project root 
```bash
DATABASE_URL=postgresql://user:password@localhost:5432/coffee_db
SECRET=your_secret_key
```
Start backend server 
```bash
uvicorn app.main:app --reload
```

### 3. Frontend Setup 
```bash
cd frontend
npm install
npm run dev
```

🧠 Project Structure

CoffeeCLI/
│
├── app/
│   ├── main.py            # FastAPI entry point
│   ├── auth/              # Auth configuration (FastAPI Users)
│   ├── models/            # SQLAlchemy models
│   ├── routes/            # API endpoints
│   ├── schemas/           # Pydantic models
│   └── database.py        # Database connection
│
├── frontend/              # React + Tailwind terminal interface
│
├── requirements.txt
└── README.md

🛠️ Roadmap
	•	Authentication system
	•	Recipe listing via API
	•	Terminal-style frontend shell
	•	Step-by-step recipe walkthroughs
	•	User favorites view
	•	Command autocomplete and syntax help
	•	Setup and deployment

🤝 Contributing

Contributions are welcome!
If you have ideas for new commands, UI improvements, or backend endpoints — open a PR or issue.


