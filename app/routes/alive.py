from fastapi import APIRouter
from app.storage.activity_store import update_alive

router = APIRouter(prefix="/alive", tags=["Alive"])

@router.post("/{user_id}")
def alive(user_id: str):
    update_alive(user_id)
    return {"status": "alive"}
