from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

from ..database import SessionLocal
from ..models import User

router = APIRouter(prefix="/heartbeat")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{phone}")
def heartbeat(phone: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone_primary == phone).first()
    if not user:
        raise HTTPException(404, "User not found")

    user.last_active_at = datetime.utcnow()
    db.commit()

    return {"message": "User marked safe"}
