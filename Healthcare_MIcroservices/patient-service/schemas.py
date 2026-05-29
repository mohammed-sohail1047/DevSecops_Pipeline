from pydantic import BaseModel, EmailStr
from datetime import datetime


class PatientBase(BaseModel):
    name: str
    email: EmailStr


class PatientCreate(PatientBase):
    password: str


class PatientOut(PatientBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
