from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    full_name:str
    email:EmailStr
    password:str
    role:str="student"
    
class UserRegister(UserBase):
    pass

class UserResponse(UserBase):
    id:int
    is_active:bool=True
    created_at:datetime
    updated_at:datetime
    profile_picture:Optional[str]=None
    
    class Config:
        from_attributes=True
        
class UserUpdate(BaseModel):
    full_name:Optional[str]=None    
    email:Optional[EmailStr]=None
    
