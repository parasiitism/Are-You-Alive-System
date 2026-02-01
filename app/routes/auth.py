from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..schemas import UserRegisterRequest, UserResponse
from ..crud import get_user_by_phone, create_user

router = APIRouter(prefix="/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserResponse)
def register_user(data: UserRegisterRequest, db: Session = Depends(get_db)):

    if not data.consent_given:
        raise HTTPException(
            status_code=400,
            detail="Consent is required to use this app"
        )

    existing_user = get_user_by_phone(db, data.phone_primary)
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User already registered"
        )

    user = create_user(db, data)
    return user
