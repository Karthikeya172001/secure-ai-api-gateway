from fastapi import APIRouter, Depends

from app.security import get_current_user
from fastapi import HTTPException

from app.prompt_filter import is_prompt_safe
from app.schemas import PromptRequest
from app.logger import log_event

from app.llm import ask_llm



router = APIRouter(tags=["Protected"])


@router.get("/profile")
def profile(current_user=Depends(get_current_user)):
    return {
        "message": "Access granted!",
        "user": current_user
    }

@router.post("/chat")
def chat(
    request: PromptRequest,
    current_user=Depends(get_current_user)
):
    safe, reason = is_prompt_safe(request.prompt)

    if not safe:
        log_event(
            current_user["sub"],
            "/chat",
            request.prompt,
            f"Blocked ({reason})"
        )

        raise HTTPException(
            status_code=400,
            detail=f"Blocked suspicious prompt: {reason}"
        )

    log_event(
        current_user["sub"],
        "/chat",
        request.prompt,
        "Allowed"
    )


    answer = ask_llm(request.prompt)

    return {
        "user": current_user["sub"],
        "response": answer
        }
