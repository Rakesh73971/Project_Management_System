from pydantic import BaseModel,EmailStr
from typing import Optional
from datetime import datetime
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True

class OrganizationMemberCreate(BaseModel):
    oragnization_id : int
    role : str

class OrganizationMemberUpdate(BaseModel):
    organization_id : Optional[str] = None
    role:Optional[str] = None

class OrganizationMemberResponse(OrganizationMemberCreate):
    id : int
    user_id : int

    class Config:
        from_attributes = True

class OrganizationCreate(BaseModel):
    name: str
    status: str
    description: str

class OrganizationUpdate(BaseModel):
    name:Optional[str] = None
    status:Optional[str] = None
    description:Optional[str] = None

class OrganizationResponse(OrganizationCreate):
    id : int
    createdAt : datetime
    updatedAt : datetime

    class Config:
        from_attributes = True


