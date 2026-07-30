# 🔐 Secure AI API Gateway

A production-inspired AI Gateway built with **FastAPI** that demonstrates secure authentication, role-based access control, prompt injection detection, audit logging, rate limiting, and AI integration.

## 🚀 Features

- ✅ User Registration
- ✅ JWT Authentication
- ✅ Password Hashing (bcrypt)
- ✅ Role-Based Access Control (RBAC)
- ✅ Protected APIs
- ✅ Prompt Injection Detection
- ✅ Audit Logging
- ✅ Admin-only Audit Log Viewer
- ✅ Rate Limiting (5 requests/minute)
- ✅ OpenAI Integration
- ✅ Swagger API Documentation
- ✅ Automated Testing using pytest

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Backend | FastAPI |
| Database | SQLite + SQLAlchemy |
| Authentication | JWT |
| Password Hashing | bcrypt |
| Validation | Pydantic |
| AI | OpenAI API |
| Rate Limiting | SlowAPI |
| Testing | pytest |
| Documentation | Swagger/OpenAPI |

---

# 📂 Project Structure

```
secure-ai-api-gateway/
│
├── app/
│   ├── admin.py
│   ├── auth.py
│   ├── database.py
│   ├── limiter.py
│   ├── llm.py
│   ├── logger.py
│   ├── main.py
│   ├── models.py
│   ├── prompt_filter.py
│   ├── routes.py
│   ├── schemas.py
│   └── security.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_chat.py
│   └── test_profile.py
│
├── audit.log
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# 🔐 Security Features

### JWT Authentication

Users authenticate using JWT tokens.

```
POST /login
```

---

### Role-Based Access Control

Normal users:

- Access `/profile`
- Access `/chat`

Admin users:

- Access `/admin/logs`

---

### Prompt Injection Detection

Suspicious prompts such as:

```
Ignore previous instructions
Reveal your system prompt
```

are automatically blocked before reaching the AI model.

---

### Audit Logging

Every chat request is stored with:

- Timestamp
- Username
- Endpoint
- Prompt
- Status

Example:

```
2026-07-28 16:24:57
User: admin
Endpoint: /chat
Status: Allowed
Prompt: What is JWT authentication?
```

---

### Rate Limiting

The chat endpoint allows:

```
5 requests / minute
```

Additional requests receive:

```
HTTP 429 Too Many Requests
```

---

# 📚 API Endpoints

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | /register |
| POST | /login |

---

## Protected

| Method | Endpoint |
|---------|----------|
| GET | /profile |
| POST | /chat |

---

## Admin

| Method | Endpoint |
|---------|----------|
| GET | /admin/logs |

---

## Utility

| Method | Endpoint |
|---------|----------|
| GET | / |
| GET | /health |

---

# 🧪 Running Tests

```bash
pytest
```

Example output:

```
==============================
4 passed
==============================
```

---

# ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/<your-username>/secure-ai-api-gateway.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
uvicorn app.main:app --reload
```

Swagger:

```
http://127.0.0.1:8000/docs
```

---

# 📈 Future Improvements

- Docker Compose
- PostgreSQL
- Redis-based Rate Limiting
- CI/CD using GitHub Actions
- Kubernetes Deployment
- OAuth Login
- Multi-tenant Support

---

# 👨‍💻 Author

**Gorityala Karthikeya**

Software Engineer

Backend Development • FastAPI • Python • AI Security