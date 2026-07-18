from pydantic import BaseModel,EmailStr
from datetime import datetime

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
    
    class Config:
        from_attributes=True