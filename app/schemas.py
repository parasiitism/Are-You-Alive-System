from pydantic import BaseModel, Field

class UserRegisterRequest(BaseModel):
    phone_primary: str = Field(..., min_length=10, max_length=15)
    phone_emergency: str = Field(..., min_length=10, max_length=15)
    consent_given: bool

class UserResponse(BaseModel):
    id: str
    phone_primary: str
    phone_emergency: str
