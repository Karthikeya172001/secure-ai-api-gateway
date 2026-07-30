# 🔐 Secure AI API Gateway

A production-ready AI API Gateway built with **FastAPI** that secures AI interactions using JWT authentication, Role-Based Access Control (RBAC), prompt injection detection, audit logging, and rate limiting.

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
| Language | Python 3.12 |
| Database | SQLite |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Password Security | bcrypt + Passlib |
| Validation | Pydantic |
| API Docs | Swagger/OpenAPI |
| Testing | Pytest |
| Rate Limiting | SlowAPI |

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
git clone https://github.com/<your-username>/secure-ai-api-gateway.git

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

# 📖 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

ReDoc:

```
http://127.0.0.1:8000/redoc
```

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
| GET | /profile | Get user profile |
| POST | /chat | AI Chat Endpoint |

---

## Admin

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /admin/logs | View Audit Logs |

---

# 🔐 Security Features

✅ JWT Authentication

✅ Password Hashing (bcrypt)

✅ Role-Based Access Control

✅ Prompt Injection Detection

✅ Audit Logging

✅ Rate Limiting

---

# 🧪 Running Tests

```bash
pytest
```

Expected:

```text
4 passed
```

---

# 📸 Screenshots

## 🏠 Swagger Home

Overview of all available API endpoints documented using Swagger UI.

![Swagger Home](screenshots/swagger-home.png)

---

## 👤 User Registration

Successful user registration through the `/register` endpoint.

![Register](screenshots/register.png)

---

## 🔑 User Login

JWT token generation after successful authentication.

![Login Success](screenshots/login-success.png)

---

## 👤 Protected Profile Endpoint

Authenticated user accessing the protected `/profile` endpoint using a valid JWT token.

![Profile Endpoint](screenshots/profile-endpoint.png)

---

## 🤖 AI Chat Endpoint

Authenticated users interacting with the AI Chat endpoint with prompt validation and security checks.

![Chat Endpoint](screenshots/chat-endpoint.png)

---

## 🔄 Password Reset

Password reset endpoint securely updating the user's password.

![Password Reset](screenshots/reset.png)

---

## 📋 Admin Audit Logs

Admin-only endpoint displaying application audit logs.

![Admin Logs](screenshots/admin-logs.png)

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

Software Engineer

- GitHub: https://github.com/Karthikeya172001
- LinkedIn: *(Add your LinkedIn profile URL here)*

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you found this project useful, please consider giving it a star!