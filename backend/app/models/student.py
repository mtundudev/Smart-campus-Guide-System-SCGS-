from app.core.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime



class Student(Base):
    
    __tablename__="students"
    
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False,unique=True)
    student_number=Column(String,nullable=False,unique=True)
    year_of_study=Column(Integer,nullable=False)
    department=Column(String,nullable=False)
    program=Column(String,nullable=False)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    user= relationship("User",back_populates="student",uselist=False)
    