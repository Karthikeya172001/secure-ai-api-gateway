# 🔐 Secure AI API Gateway

A security-focused AI API Gateway built with **Python, FastAPI, and Groq**.

The gateway provides JWT authentication, role-based access control (RBAC), prompt-injection detection, rate limiting, audit logging, and controlled access to LLM APIs.

This project demonstrates backend engineering and AI security concepts including secure authentication, authorization, API security, LLM integration, database management, automated testing, and cloud deployment.

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

📖 How It Works
1. A user registers an account.
2. The user logs in and receives a JWT access token.
3. Protected endpoints validate the JWT token.
4. RBAC determines whether the user has permission to access an endpoint.
5. Rate limiting controls API request volume.
6. Prompts sent to the AI endpoint are analyzed for potential prompt injection.
7. Safe prompts are forwarded to the configured Groq LLM.
8. The AI response is returned to the client.
9. Important system activities are recorded through audit logging.
🛡️ Security Testing
The deployed API was tested through Swagger UI to verify the implemented security controls.
🔐 JWT Authentication
GET /profile
→ 200 OK

👤 Role-Based Access Control
A normal user attempting to access the admin endpoint is rejected:
GET /admin/logs
→ 403 Forbidden
→ Admin access required

🚨 Prompt Injection Detection
A prompt attempting to reveal system instructions is blocked:
POST /chat
→ 400 Bad Request
→ Blocked suspicious prompt

⏱️ Rate Limiting
The /chat endpoint enforces a limit of 5 requests per minute:
POST /chat
→ 429 Too Many Requests
→ Rate limit exceeded: 5 per 1 minute

🤖 Successful AI Request
Valid authenticated prompts are processed successfully:
POST /chat
→ 200 OK
→ AI response

📸 Screenshots
🏠 Swagger UI

👤 User Registration

🔑 User Login

👤 Protected Profile

🤖 AI Chat

🔄 Password Reset

📋 Admin Audit Logs

📂 Project Structure
secure-ai-api-gateway/
│
├── app/
│   ├── __init__.py
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
├── screenshots/
├── tests/
├── .gitignore
├── Dockerfile
├── pytest.ini
├── render.yaml
├── requirements.txt
└── README.md

⚙️ Local Setup
1. Clone the repository
git clone https://github.com/Karthikeya172001/secure-ai-api-gateway.git
cd secure-ai-api-gateway

2. Create a virtual environment
python -m venv .venv

3. Activate the virtual environment
Windows
.venv\Scripts\activate

Linux / macOS
source .venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

5. Configure environment variables
Create a .env file:
SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_api_key

Never commit real API keys, JWT secrets, passwords, or other credentials to GitHub.
6. Run the application
uvicorn app.main:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

📡 API Endpoints
Authentication
Method	Endpoint	Description
POST	/register	Register a new user
POST	/login	Login and receive JWT
PUT	/reset-password	Reset password


Protected
Method	Endpoint	Description
GET	/profile	Get authenticated user profile
POST	/chat	Send a prompt to the AI service


Admin
Method	Endpoint	Description
GET	/admin/logs	View audit logs


System
Method	Endpoint	Description
GET	/	API root
GET	/health	Health check


🔒 Security
The project implements several API security mechanisms:
- JWT authentication
- Password hashing
- Role-Based Access Control
- Protected endpoints
- Rate limiting
- Prompt-injection detection
- Audit logging
- Environment-based secret management
- HTTPS deployment
🤖 AI Integration
The gateway integrates with Groq's OpenAI-compatible API using the configured openai/gpt-oss-20b model.
Example Request
{
  "prompt": "What is JWT Authentication?"
}

Example Response
{
  "user": "authenticated_user",
  "response": "AI-generated response..."
}

🧪 Running Tests
Run the test suite with:
pytest

The project uses Pytest for automated testing.
🚀 Future Improvements
- Refresh-token rotation
- Email verification
- Docker and container improvements
- CI/CD with GitHub Actions
- PostgreSQL support
- Redis-based rate limiting
- API key management
- AI risk scoring
- Personally Identifiable Information (PII) detection
- Advanced prompt-injection detection
- Security monitoring and alerting
👨‍💻 Author
Gorityala Karthikeya
Software Engineer focused on Python backend development, FastAPI, AI/LLM applications, authentication, and API security.
📧 Email: gorityalakarthikey@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/karthikeya-gorityala
💻 GitHub: https://github.com/Karthikeya172001
🌐 Live API: https://secure-ai-api-gateway.onrender.com
📖 Swagger UI: https://secure-ai-api-gateway.onrender.com/docs
📄 License
This project is licensed under the MIT License.
⭐ Support
If you found this project useful, consider giving it a ⭐ on GitHub.
```
