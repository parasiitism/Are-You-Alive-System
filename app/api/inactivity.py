from fastapi import APIRouter
from app.inactivity import InactivityEngine

router = APIRouter(prefix="/inactivity", tags=["Inactivity"])


@router.get("/check")
def check_inactivity():
    inactive_users = InactivityEngine.find_inactive_users()
    return {
        "inactive_count": len(inactive_users),
        "users": inactive_users
    }
