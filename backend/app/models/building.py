from app.core.database import Base
from sqlalchemy import Column,Integer,String,DateTime,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class Building(Base):
    __tablename__="buidings"
    id= Column(Integer,primary_key=True,index=True)
    
    name=Column(String,nullable=True)# LIBRARY
    code=Column(String,nullable=False,unique=True)#ADM,LIB
    description=Column(String(255),nullable=False)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    floor=relationship("Floor",back_populates="buildigs",cascade="all, delete-orphan")