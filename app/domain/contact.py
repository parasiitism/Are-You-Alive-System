from pydantic import BaseModel

class Contact(BaseModel):
    phone: str
    email: str
