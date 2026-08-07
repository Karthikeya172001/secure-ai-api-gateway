# 🔐 Secure AI API Gateway

A production-ready AI API Gateway built using **Python**, **FastAPI**, and **Groq Llama 3.1**. The project secures AI interactions through **JWT Authentication**, **Role-Based Access Control (RBAC)**, **Prompt Injection Detection**, **Audit Logging**, **Rate Limiting**, and **RESTful APIs**.

This project demonstrates backend software engineering concepts including secure authentication, AI integration, API security, prompt filtering, audit logging, database management, and cloud deployment.

---

# 🚀 Live Demo

| Service | URL |
|---------|-----|
| 🌐 Live API | https://secure-ai-api-gateway.onrender.com |
| 📖 Swagger UI | https://secure-ai-api-gateway.onrender.com/docs |
| 📚 ReDoc | https://secure-ai-api-gateway.onrender.com/redoc |
| ❤️ Health Check | https://secure-ai-api-gateway.onrender.com/health |
| 💻 GitHub Repository | https://github.com/Karthikeya172001/secure-ai-api-gateway |

---

# ✨ Features

- 🔑 User Registration
- 🔐 JWT Authentication
- 👤 Role-Based Access Control (RBAC)
- 🔒 Password Hashing using bcrypt
- 🔄 Password Reset
- 🛡 Protected API Endpoints
- 🤖 AI Chat using Groq Llama 3.1
- 🚨 Prompt Injection Detection
- 📝 Audit Logging
- ⏱ Rate Limiting
- 📖 Interactive Swagger Documentation
- ☁ Live Deployment on Render
- ✅ Unit Testing with Pytest

---

# 🛠 Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python 3.x |
| Backend | FastAPI |
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

# 🏗 Architecture

```text
                 Client
                    │
                    ▼
          FastAPI REST API
                    │
      JWT Authentication & RBAC
                    │
    Prompt Injection Detection
                    │
         Groq Llama 3.1 API
                    │
            Audit Logging
                    │
             SQLite Database
```

---

# 📖 How It Works

1. A user registers a new account.
2. The user logs in and receives a JWT access token.
3. Protected API endpoints validate the JWT token.
4. Role-Based Access Control (RBAC) determines user permissions.
5. Prompt Injection Detection analyzes prompts before they are sent to the AI model.
6. Safe prompts are forwarded to the Groq Llama 3.1 model.
7. AI-generated responses are returned to the user.
8. Audit logs record important system activities.

---

# 📸 Screenshots

### 🏠 Swagger Home

![Swagger Home](screenshots/swagger-home.png)

---

### 👤 User Registration

![User Registration](screenshots/register.png)

---

### 🔑 User Login

![User Login](screenshots/login.png)

---

### 👤 Protected Profile

![Protected Profile](screenshots/profile.png)

---

### 🤖 AI Chat

![AI Chat](screenshots/chat.png)

---

### 🔄 Password Reset

![Password Reset](screenshots/reset-password.png)

---

### 📋 Admin Audit Logs

![Admin Audit Logs](screenshots/admin-logs.png)

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

# ⚙ Local Setup

Clone the repository:

```bash
git clone https://github.com/Karthikeya172001/secure-ai-api-gateway.git
```

Navigate to the project:

```bash
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

### Linux/macOS

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

# 📡 API Endpoints

## Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login and receive JWT |
| PUT | `/reset-password` | Reset password |

## Protected

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/profile` | Get authenticated user profile |
| POST | `/chat` | AI Chat Endpoint |

## Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin/logs` | View Audit Logs |

---

# 🔒 Security Features

- JWT Authentication
- Password Hashing using bcrypt
- Role-Based Access Control (RBAC)
- Prompt Injection Detection
- Audit Logging
- Rate Limiting
- Protected REST APIs

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

# 🚀 Future Improvements

- Refresh Tokens
- Email Verification
- Docker Support
- CI/CD with GitHub Actions
- PostgreSQL Support
- Redis Caching
- API Key Management
- AI Risk Scoring
- Personally Identifiable Information (PII) Detection

---

# 👨‍💻 Author

**Gorityala Karthikeya**

📧 Email: gorityalakarthikeya@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/karthikeya-gorityala

💻 GitHub: https://github.com/Karthikeya172001

🌐 Live API: https://secure-ai-api-gateway.onrender.com

📖 Swagger UI: https://secure-ai-api-gateway.onrender.com/docs

---

# 📄 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.
