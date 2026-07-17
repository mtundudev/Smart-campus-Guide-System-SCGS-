from app.core.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class Floor(Base):
    
    __tablename__="floors"
    id=Column(Integer,primary_key=True,index=True)
    buiding_id=Column(Integer,ForeignKey("buidings.id",ondelete="CASCADE"),nullable=False)
    floor_number=Column(Integer,nullable=True)
    floor_name=Column(String,nullable=False)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    building=relationship("Building",back_populates="floor")
    room=relationship("Room",back_populates="floor",cascade="all,delete-orphan")