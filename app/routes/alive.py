from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime

from app.database import get_db
from app.models.user import User

router = APIRouter()

@router.post("/alive/{user_id}")
def alive(user_id: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "User not found"}

    user.last_alive_at = datetime.utcnow()
    db.commit()

    return {
        "status":"ok",
        "message":"Glad to hear about you ❤️",
        "last_alive_at":user.last_alive_at
    }
