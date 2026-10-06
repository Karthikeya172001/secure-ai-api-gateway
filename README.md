# 🔐 Secure AI API Gateway

A secure AI API Gateway built with **Python, FastAPI, and Groq Llama 3.1**.

The gateway provides authentication, authorization, API security, prompt injection detection, audit logging, rate limiting, and AI-powered REST APIs.

This project demonstrates backend engineering concepts including **secure authentication, RBAC, API security, AI/LLM integration, database management, automated testing, and cloud deployment**.

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
- 🛡 Protected REST API endpoints
- 🤖 AI chat using Groq Llama 3.1
- 🚨 Prompt injection detection
- 📝 Audit logging
- ⏱ Rate limiting
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
| AI | Groq / Llama 3.1 |
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
              ┌───────┴────────┐
              │                │
        Rate Limiting      Authentication
                                 │
                          JWT + RBAC
                                 │
                    ┌────────────┴────────────┐
                    │                         │
             Protected APIs             Admin APIs
                    │                         │
                    ▼                         ▼
             Prompt Detection          Audit Logging
                    │
                    ▼
             Groq Llama 3.1
                    │
                    ▼
              AI Response

                 SQLite
                    ▲
                    │
             Application Data
```

---

## 📖 How It Works

1. A user registers an account.
2. The user logs in and receives a JWT access token.
3. Protected endpoints validate the JWT token.
4. RBAC determines whether the user has permission to access an endpoint.
5. Rate limiting helps control API request volume.
6. Prompts sent to the AI endpoint are analyzed for potential prompt injection.
7. Safe prompts are forwarded to the Groq Llama 3.1 model.
8. The AI response is returned to the client.
9. Important system activities are recorded through audit logging.

---

## 📸 Screenshots

### 🏠 Swagger UI

![Swagger Home](screenshots/swagger-home.png)

### 👤 User Registration

![User Registration](screenshots/register.png)

### 🔑 User Login

![User Login](screenshots/login-success.png)

### 👤 Protected Profile

![Protected Profile](screenshots/profile-endpoint.png)

### 🤖 AI Chat

![AI Chat](screenshots/chat-endpoint.png)

### 🔄 Password Reset

![Password Reset](screenshots/reset.png)

### 📋 Admin Audit Logs

![Admin Audit Logs](screenshots/admin-logs.png)

---

## 📂 Project Structure

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

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Karthikeya172001/secure-ai-api-gateway.git
cd secure-ai-api-gateway
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_api_key
```

Never commit real API keys or secrets to GitHub.

### 6. Run the application

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT |
| PUT | `/reset-password` | Reset password |

### Protected

| Method | Endpoint | Description |
|---|---|---|
| GET | `/profile` | Get authenticated user profile |
| POST | `/chat` | Send a prompt to the AI service |

### Admin

| Method | Endpoint | Description |
|---|---|---|
| GET | `/admin/logs` | View audit logs |

---

## 🔒 Security

The project implements several API security mechanisms:

- JWT authentication
- Password hashing
- Role-Based Access Control
- Protected endpoints
- Rate limiting
- Prompt injection detection
- Audit logging

---

## 🤖 AI Integration

The gateway integrates with **Groq's OpenAI-compatible API** using the **Llama 3.1** model.

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

## 🧪 Running Tests

Run:

```bash
pytest
```

Make sure the test result shown here matches the current repository before adding a specific expected count.

---

## 🚀 Future Improvements

- Refresh tokens
- Email verification
- Docker support
- CI/CD with GitHub Actions
- PostgreSQL support
- Redis caching
- API key management
- AI risk scoring
- Personally Identifiable Information (PII) detection

---

## 👨‍💻 Author

**Gorityala Karthikeya**

📧 gorityalakarthikeya@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/karthikeya-gorityala

💻 GitHub: https://github.com/Karthikeya172001

🌐 Live API: https://secure-ai-api-gateway.onrender.com

📖 Swagger UI: https://secure-ai-api-gateway.onrender.com/docs

---

## 📄 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
