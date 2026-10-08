from fastapi import APIRouter, Depends, HTTPException, Request

from app.security import get_current_user
from app.prompt_filter import is_prompt_safe
from app.schemas import PromptRequest
from app.logger import log_event
from app.llm import ask_llm
from app.limiter import limiter

router = APIRouter(tags=["Protected"])


@router.get(
    "/profile",
    responses={
        401: {"description": "Authentication required"},
    },
)
def profile(current_user=Depends(get_current_user)):
    return {
        "message": "Access granted!",
        "user": current_user
    }


@router.post(
    "/chat",
    responses={
        400: {"description": "Suspicious prompt blocked"},
        401: {"description": "Authentication required"},
        429: {"description": "Rate limit exceeded"},
        502: {"description": "AI service unavailable"},
    },
)
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

    try:
        answer = ask_llm(prompt_request.prompt)
    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI service is currently unavailable"
        )

    return {
        "user": current_user["sub"],
        "response": answer
    }
