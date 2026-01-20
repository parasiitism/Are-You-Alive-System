from fastapi import APIRouter
from app.domain.user import User
from app.storage.user_store import save_user

router = APIRouter(prefix="/user", tags=["User"])

@router.post("/register")
def register_user(user: User):
    save_user(user)
    return {"status": "registered"}
