from sqlalchemy import Column, String, DateTime, Boolean, Integer
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)

    last_alive_at = Column(DateTime, default=datetime.utcnow)
    alive_interval_hours = Column(Integer, default=48)

    location_enabled = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
