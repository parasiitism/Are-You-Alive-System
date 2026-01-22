from sqlalchemy import Column, String, Integer, ForeignKey
from app.database import Base

class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"

    id = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))

    name = Column(String)
    phone = Column(String)
    email = Column(String)
    priority = Column(Integer, default=1)
