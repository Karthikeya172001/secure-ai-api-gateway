from fastapi import APIRouter, Depends

from app.security import get_current_user
from fastapi import HTTPException

from app.prompt_filter import is_prompt_safe
from app.schemas import PromptRequest
from app.logger import log_event

from app.llm import ask_llm

from fastapi import Request
from app.limiter import limiter

router = APIRouter(tags=["Protected"])


@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return {
        "message": "Access granted!",
        "user": current_user
    }

@router.post("/chat")
@limiter.limit("5/minute")
def chat(
    request: Request,
    prompt_request: PromptRequest,
    current_user=Depends(get_current_user),
):
    safe, reason = is_prompt_safe(prompt_request.prompt)

    if not safe:
        log_event(
            current_user["sub"],
            "/chat",
            prompt_request.prompt,
            f"Blocked ({reason})"
        )

        raise HTTPException(
            status_code=400,
            detail=f"Blocked suspicious prompt: {reason}"
        )

    log_event(
        current_user["sub"],
        "/chat",
        prompt_request.prompt,
        "Allowed"
    )

    answer = ask_llm(prompt_request.prompt)

    return {
        "user": current_user["sub"],
        "response": answer
    }