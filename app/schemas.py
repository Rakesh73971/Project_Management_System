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
    user_id : int
    organization_id : int
    role : str

class OrganizationMemberUpdate(BaseModel):
    organization_id : Optional[str] = None
    role:Optional[str] = None

class OrganizationMemberResponse(OrganizationMemberCreate):
    id : int
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


class ProjectCreate(BaseModel):
    name : str
    organizationId : int
    status : str
    description: str

class ProjectUpdate(BaseModel):
    name : Optional[str] = None
    organizationId : Optional[int] = None
    status : Optional[str] = None
    description: Optional[str] = None
class ProjectResponse(ProjectCreate):
    id : int
    createdAt : datetime
    updatedAt : datetime

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    id : Optional[int] = None
    

class TaskCreate(BaseModel):
    project_id : int
    assigned_to : int
    status : str
    priority : str
    description: str

class TaskUpdate(BaseModel):
    project_id : Optional[int] = None
    assigned_to : Optional[int] = None
    status : Optional[str] = None
    priority: Optional[str] = None
    description: Optional[str] = None

class TaskResponse(TaskCreate):
    id : int
    createdAt : datetime
    updatedAt : datetime

    class Config:
        from_attributes = True