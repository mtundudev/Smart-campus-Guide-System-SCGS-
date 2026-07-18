from app.core.database import Base
from sqlalchemy import Column,Integer,String,DateTime,Enum,Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class RoleEnum(str,enum.Enum):
    admin="ADMIN"
    staff="STAFF"
    student="STUDENT"
    visitor="VISITOR"

class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,index=True)
    full_name=Column(String,nullable=False)
    password=Column(String,nullable=False,index=True)
    email=Column(String,unique=True,index=True,nullable=False)
    role=Column(Enum(RoleEnum,name="user_role_enum"),default=RoleEnum.student,nullable=False)
    is_active=Column(Boolean,default=True,nullable=False)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    student= relationship("Student",back_populates="user")
    audit= relationship("Audit_log",back_populates="user")