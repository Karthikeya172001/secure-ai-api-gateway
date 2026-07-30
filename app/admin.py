from fastapi import APIRouter, Depends, HTTPException
from pathlib import Path

from app.security import admin_required

router = APIRouter(tags=["Admin"])


@router.get("/admin/logs")
def get_logs(current_user=Depends(admin_required)):
    log_file = Path("audit.log")

    if not log_file.exists():
        raise HTTPException(
            status_code=404,
            detail="Audit log not found",
        )

    with open(log_file, "r") as f:
        logs = f.readlines()

    return {
        "admin": current_user["sub"],
        "logs": logs,
    }