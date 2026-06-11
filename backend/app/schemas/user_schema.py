from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    phone: str
    email: Optional[EmailStr] = None

    password: str

    student_name: str
    student_age: int

    parent_name: str
    parent_phone: str


class UserLogin(BaseModel):
    phone: str
    password: str


class UserResponse(BaseModel):
    id: int
    phone: str
    student_name: str

    class Config:
        from_attributes = True