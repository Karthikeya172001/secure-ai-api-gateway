# 🔐 Secure AI API Gateway

A production-ready AI API Gateway built with **FastAPI** that secures AI interactions using JWT authentication, Role-Based Access Control (RBAC), prompt injection detection, audit logging, and rate limiting.

---

## 🌐 Live Demo

| Service | URL |
|---------|-----|
| 🚀 Live API | https://secure-ai-api-gateway.onrender.com |
| 📖 Swagger UI | https://secure-ai-api-gateway.onrender.com/docs |
| 📚 ReDoc | https://secure-ai-api-gateway.onrender.com/redoc |

---

## 🚀 Features

- 🔑 User Registration
- 🔐 JWT Authentication
- 👤 Role-Based Access Control (RBAC)
- 🔒 Password Hashing with bcrypt
- 🔄 Password Reset
- 🛡️ Protected API Endpoints
- 🤖 AI Chat Endpoint
- 🚨 Prompt Injection Detection
- 📝 Audit Logging
- ⏱️ Rate Limiting
- 📖 Interactive Swagger Documentation
- ✅ Unit Testing with Pytest

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Language | Python 3.x |
| Database | SQLite |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Password Security | bcrypt + Passlib |
| Validation | Pydantic |
| API Docs | Swagger/OpenAPI |
| Testing | Pytest |
| Rate Limiting | SlowAPI |
| Deployment | Render |

---

# 📂 Project Structure

```text
secure-ai-api-gateway/
│
├── app/
│   ├── admin.py
│   ├── auth.py
│   ├── database.py
│   ├── limiter.py
│   ├── llm.py
│   ├── main.py
│   ├── models.py
│   ├── routes.py
│   ├── schemas.py
│   ├── security.py
│   └── utils.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_chat.py
│   └── test_profile.py
│
├── requirements.txt
├── README.md
└── screenshots/
```

---

# 🏗️ Architecture

```text
                 Client
                    │
                    ▼
          FastAPI Application
                    │
        JWT Authentication
                    │
      Role-Based Access Control
                    │
      Prompt Injection Detection
                    │
            AI Chat Endpoint
                    │
            Audit Logging
                    │
            SQLite Database
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Karthikeya172001/secure-ai-api-gateway.git

cd secure-ai-api-gateway
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

---

# ☁️ Deployment

This application is deployed on **Render**.

**Live URL**

https://secure-ai-api-gateway.onrender.com

---

# 📖 API Documentation

Swagger UI

https://secure-ai-api-gateway.onrender.com/docs

ReDoc

https://secure-ai-api-gateway.onrender.com/redoc

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register a new user |
| POST | /login | Login and receive JWT |
| PUT | /reset-password | Reset password |

---

## Protected

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /profile | Get authenticated user profile |
| POST | /chat | AI Chat Endpoint |

---

## Admin

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /admin/logs | View Audit Logs |

---

# 🔐 Security Features

- ✅ JWT Authentication
- ✅ Password Hashing (bcrypt)
- ✅ Role-Based Access Control (RBAC)
- ✅ Prompt Injection Detection
- ✅ Audit Logging
- ✅ Rate Limiting

---

# 🧪 Running Tests

```bash
pytest
```

Expected output:

```text
4 passed
```

---

# 📸 Screenshots

## 🏠 Swagger Home

![Swagger Home](screenshots/swagger-home.png)

---

## 👤 User Registration

![Register](screenshots/register.png)

---

## 🔑 User Login

![Login Success](screenshots/login-success.png)

---

## 👤 Protected Profile Endpoint

![Profile Endpoint](screenshots/profile-endpoint.png)

---

## 🤖 AI Chat Endpoint

![Chat Endpoint](screenshots/chat-endpoint.png)

---

## 🔄 Password Reset

![Password Reset](screenshots/reset.png)

---

## 📋 Admin Audit Logs

![Admin Logs](screenshots/admin-logs.png)

---

# 🚀 Future Enhancements

- Refresh Tokens
- Email-based Password Reset
- Docker Support
- CI/CD using GitHub Actions
- PostgreSQL Support
- AI Risk Scoring
- PII Detection
- API Key Management

---

# 👨‍💻 Author

**Gorityala Karthikeya**

Software Engineer | Backend Developer | Python | FastAPI

- GitHub: https://github.com/Karthikeya172001
- LinkedIn: https://www.linkedin.com/in/YOUR-LINKEDIN/

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, please consider giving it a star!