from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.location import Location
import uuid

router = APIRouter()

@router.post("/location/{user_id}")
def save_location(user_id: str, payload: dict, db: Session = Depends(get_db)):
    loc = Location(
        id=str(uuid.uuid4()),
        user_id=user_id,
        latitude=payload["lat"],
        longitude=payload["lng"],
        accuracy=payload.get("accuracy", 0)
    )

    db.add(loc)
    db.commit()
    return {"status": "location saved"}
