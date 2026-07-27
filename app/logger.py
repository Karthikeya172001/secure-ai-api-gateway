from datetime import datetime

LOG_FILE = "audit.log"

def log_event(user, endpoint, prompt, status):
    with open(LOG_FILE, "a") as file:
        file.write(
            f"{datetime.now()} | User: {user} | Endpoint: {endpoint} | Status: {status} | Prompt: {prompt}\n"
        )