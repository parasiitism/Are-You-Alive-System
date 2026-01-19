from fastapi import APIRouter
from datetime import datetime
from app.services.heartbeat_service import HEARTBEAT_STORE

router = APIRouter(
    prefix="/inactivity",
    tags=["Inactivity"]
)

@router.get("/check")
def check_inactive_users():
    now = datetime.utcnow()
    users = []

    for user_id, last_seen in HEARTBEAT_STORE.items():
        users.append({
            "user_id": user_id,
            "last_seen": last_seen.isoformat(),
            "inactive_minutes": int(
                (now - last_seen).total_seconds() / 60
            )
        })

    return {
        "count": len(users),
        "users": users
    }
