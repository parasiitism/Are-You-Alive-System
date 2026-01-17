from fastapi import APIRouter
from app.services.heartbeat_service import HeartbeatService

router = APIRouter(prefix="/heartbeat", tags=["Heartbeat"])


@router.post("/{user_id}")
def heartbeat(user_id: str):
    HeartbeatService.record(user_id)
    return {"status": "alive"}
