from sqlalchemy import Column, String, Boolean, DateTime, Integer
from datetime import datetime
import uuid
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    phone_primary = Column(String, unique=True, nullable=False)
    phone_emergency = Column(String, nullable=False)

    consent_given = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)   # 👈 OTP verified

    last_active_at = Column(DateTime, default=datetime.utcnow)
    inactive_threshold_hours = Column(Integer, default=48)

    created_at = Column(DateTime, default=datetime.utcnow)
