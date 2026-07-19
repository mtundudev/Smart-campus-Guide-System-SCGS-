from app.core.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class Room(Base):
    __tablename__="rooms"
    id=Column(Integer,primary_key=True,unique=True)
    floor_id=Column(Integer,ForeignKey("floors.id",ondelete="CASCADE"),nullable=True)
    room_name=Column(String,nullable=False,unique=True)
    room_number=Column(Integer,nullable=False)
    room_type=Column(String,nullable=False)
    capacity=Column(Integer,nullable=True)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    floor=relationship("Floor",back_populates="room")
    #location=relationship("Location",back_populates="room",cascade="all, delete-orphan")
    
    