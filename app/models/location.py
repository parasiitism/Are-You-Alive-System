from sqlalchemy import Column, String, Float, DateTime
from app.database import Base
from datetime import datetime

class Location(Base):
    __tablename__ = "locations"

    id = Column(String, primary_key=True)
    user_id = Column(String)

    latitude = Column(Float)
    longitude = Column(Float)
    accuracy = Column(Float)

    recorded_at = Column(DateTime, default=datetime.utcnow)
