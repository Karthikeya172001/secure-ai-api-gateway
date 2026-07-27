SUSPICIOUS_PATTERNS = [
    "ignore previous instructions",
    "system prompt",
    "developer mode",
    "bypass",
    "jailbreak",
    "reveal your prompt",
    "forget previous instructions",
]

def is_prompt_safe(prompt: str):
    lower_prompt = prompt.lower()

    for pattern in SUSPICIOUS_PATTERNS:
        if pattern in lower_prompt:
            return False, pattern

    return True, None