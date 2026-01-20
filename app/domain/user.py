from pydantic import BaseModel
from app.domain.contact import Contact

class User(BaseModel):
    user_id: str
    emergency_contact: Contact
