# 📊 Summer Project 2025 — Streamlit + FastAPI + AI

A full-stack Python project featuring user authentication (with facial recognition), role-based dashboards, and an AI-powered chatbot that answers natural language questions by converting them into SQL queries.

---

## 🚀 Features

### 🔐 Authentication

* Sign-up and Login via Email & Password
* Facial recognition authentication using `face_recognition`
* Role-based redirection: `admin` vs `user`

### 🧠 AI Chatbot

* Ask natural language questions ("Show me sessions from June")
* Powered by **Perplexity/OpenAI LLMs**
* Converts questions → SQL → fetches data from PostgreSQL

### 📈 Session Dashboard

* Real-time session data (charts + tables)
* Sidebar filters for intuitive session search
* Dual views: `Details` and `Metrics`

### 🛠 Admin Panel

* View registered users
* Onboard new users via UI
* Role management with default as `user`

### 🧹 Modular Backend Structure

```bash
backend/
├── api/                # FastAPI endpoints (auth, admin, chat, session)
├── assistant/          # SQL generator + system prompt for LLMs
├── auth/               # Facial recognition & user management
├── dao/                # PostgreSQL interaction modules
├── models/llm/         # LLM interface: OpenAI, Perplexity
├── utils/              # Logging and helpers
```

### 💻 Frontend Structure

```bash
frontend/
├── pages/              # Core Streamlit views: login, signup, dashboard, etc.
├── admin/, chat/, dashboard/  # Role-specific UI modules
├── dashboard/sidebar.py       # Sidebar filter controls
```

---

## 🧰 Tech Stack

| Layer      | Technology                |
| ---------- | ------------------------- |
| Frontend   | Streamlit                 |
| Backend    | FastAPI                   |
| Database   | PostgreSQL                |
| LLM        | Perplexity / OpenAI       |
| Auth       | face\_recognition, bcrypt |
| Deployment | Docker + Ngrok            |

---

## 📂 How to Run

### 🔧 1. Install Requirements

```bash
pip install -r requirements.txt
```

### 🚀 2. Run Backend (FastAPI)

```bash
uvicorn backend.api.main:app --reload
```

### 🌐 3. Run Frontend (Streamlit)

```bash
streamlit run app.py
```

---

## 🙌 Author

**Daksh Khanna**
[LinkedIn]([(https://www.linkedin.com/in/daksh-khanna-769002320/)](https://www.linkedin.com/in/daksh-khanna-769002320/)) | [GitHub](https://github.com/Daksh-Khanna)

---

## 📌 License

This project is licensed under the **MIT License**.

You're free to use, modify, and distribute the code with attribution. See the [LICENSE](https://opensource.org/licenses/MIT) for details.
