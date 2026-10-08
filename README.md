# 🔐 Secure AI API Gateway

A security-focused AI API Gateway built with **Python, FastAPI, and Groq**.

The gateway provides JWT authentication, role-based access control (RBAC),
prompt-injection detection, rate limiting, audit logging, and controlled
access to LLM APIs.

This project demonstrates backend engineering and AI security concepts
including secure authentication, authorization, API security, LLM integration,
database management, automated testing, and cloud deployment.

---

## 🚀 Live Demo

| Service | URL |
|---|---|
| 🌐 Live API | https://secure-ai-api-gateway.onrender.com |
| 📖 Swagger UI | https://secure-ai-api-gateway.onrender.com/docs |
| 📚 ReDoc | https://secure-ai-api-gateway.onrender.com/redoc |
| ❤️ Health Check | https://secure-ai-api-gateway.onrender.com/health |
| 💻 GitHub | https://github.com/Karthikeya172001/secure-ai-api-gateway |

---

## ✨ Features

- 🔑 User registration
- 🔐 JWT authentication
- 👤 Role-Based Access Control (RBAC)
- 🔒 Password hashing using bcrypt
- 🔄 Password reset
- 🛡️ Protected REST API endpoints
- 🤖 AI chat using Groq (`openai/gpt-oss-20b`)
- 🚨 Prompt-injection detection
- 📝 Audit logging
- ⏱️ Rate limiting
- 📖 Swagger / OpenAPI documentation
- ☁️ Cloud deployment on Render
- 🧪 Automated testing with Pytest

---

## 🛠️ Technologies

| Category | Technology |
|---|---|
| Language | Python 3.x |
| Backend | FastAPI |
| Database | SQLite |
| ORM | SQLAlchemy |
| Authentication | JWT |
| Password Security | bcrypt / Passlib |
| Validation | Pydantic |
| AI | Groq / `openai/gpt-oss-20b` |
| API Documentation | Swagger / OpenAPI |
| Testing | Pytest |
| Rate Limiting | SlowAPI |
| Deployment | Render |

---

## 🏗️ Architecture

```text
                         Client
                           │
                           ▼
                   FastAPI REST API
                           │
              ┌────────────┴────────────┐
              │                         │
       Rate Limiting              Authentication
                                      │
                                JWT + RBAC
                                      │
                         ┌────────────┴────────────┐
                         │                         │
                  Protected APIs              Admin APIs
                         │                         │
                         ▼                         ▼
                Prompt Detection           Audit Logging
                         │
                         ▼
                     Groq LLM
                         │
                         ▼
                    AI Response

                         SQLite
                            ▲
                            │
                     Application Data
