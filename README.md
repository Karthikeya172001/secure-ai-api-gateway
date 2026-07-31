# 🔐 Secure AI API Gateway

A production-ready AI API Gateway built with **FastAPI** that secures AI interactions using JWT Authentication, Role-Based Access Control (RBAC), Prompt Injection Detection, Audit Logging, Rate Limiting, and AI-powered responses using **Groq Llama 3.1**.

---

## 🌐 Live Demo

| Service | URL |
|---------|-----|
| 🚀 Live API | https://secure-ai-api-gateway.onrender.com |
| 📖 Swagger UI | https://secure-ai-api-gateway.onrender.com/docs |
| 📚 ReDoc | https://secure-ai-api-gateway.onrender.com/redoc |
| ❤️ Health Check | https://secure-ai-api-gateway.onrender.com/health |

---

## 🚀 Features

- 🔑 User Registration
- 🔐 JWT Authentication
- 👤 Role-Based Access Control (RBAC)
- 🔒 Password Hashing with bcrypt
- 🔄 Password Reset
- 🛡️ Protected API Endpoints
- 🤖 AI Chat using Groq Llama 3.1
- 🚨 Prompt Injection Detection
- 📝 Audit Logging
- ⏱️ Rate Limiting
- 📖 Interactive Swagger Documentation
- ☁️ Live Deployment on Render
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
| AI | Groq (Llama 3.1) |
| API Documentation | Swagger / OpenAPI |
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
├── screenshots/
├── requirements.txt
└── README.md
```

---

# 🏗️ Architecture

```text
                    Client
                       │
                       ▼
             FastAPI Application
                       │
        JWT Authentication & RBAC
                       │
      Prompt Injection Detection
                       │
             AI Gateway (Groq)
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

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

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

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_api_key
```

Run the application:

```bash
uvicorn app.main:app --reload
```

---

# ☁️ Deployment

This project is deployed on **Render**.

**Live URL**

https://secure-ai-api-gateway.onrender.com

---

# 📖 API Documentation

**Swagger UI**

https://secure-ai-api-gateway.onrender.com/docs

**ReDoc**

https://secure-ai-api-gateway.onrender.com/redoc

---

# 📌 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | /register | Register a new user |
| POST | /login | Login and receive JWT |
| PUT | /reset-password | Reset password |

### Protected

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | /profile | Get authenticated user profile |
| POST | /chat | AI Chat Endpoint |

### Admin

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

# 🤖 AI Integration

This project integrates with **Groq's OpenAI-compatible API** using the **Llama 3.1** model to generate AI-powered responses.

### Example Request

```json
{
  "prompt": "What is JWT Authentication?"
}
```

### Example Response

```json
{
  "user": "karthik",
  "response": "JWT (JSON Web Token) is a secure method for transmitting information between parties..."
}
```

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

![Login](screenshots/login-success.png)

---

## 👤 Protected Profile

![Profile](screenshots/profile-endpoint.png)

---

## 🤖 AI Chat

![Chat](screenshots/chat-endpoint.png)

---

## 🔄 Password Reset

![Password Reset](screenshots/reset.png)

---

## 📋 Admin Audit Logs

![Admin Logs](screenshots/admin-logs.png)

---

# 🚀 Future Enhancements

- Refresh Tokens
- Email Verification
- Docker Support
- CI/CD using GitHub Actions
- PostgreSQL Support
- Redis Caching
- API Key Management
- AI Risk Scoring
- PII Detection

---

# 👨‍💻 Author

## Gorityala Karthikeya

Software Engineer | Backend Developer | Python | FastAPI | AI

### 🔗 Connect with Me

- 💻 **GitHub:** https://github.com/Karthikeya172001
- 💼 **LinkedIn:** https://www.linkedin.com/in/karthikeya-gorityala/
- 🚀 **Live Demo:** https://secure-ai-api-gateway.onrender.com
- 📖 **Swagger UI:** https://secure-ai-api-gateway.onrender.com/docs

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.