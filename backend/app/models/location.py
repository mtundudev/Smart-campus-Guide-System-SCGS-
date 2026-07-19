from app.core.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,Float,Boolean,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class Location(Base):
    __tablename__="locations"
    
    id=Column(Integer,primary_key=True,index=True)
    room_id=Column(Integer,ForeignKey("rooms.id",ondelete="CASCADE"),unique=True)
    latitude=Column(Float,nullable=True)
    longitude=Column(Float,nullable=True)
    is_accessible=Column(Boolean,default=True)
    indoor=Column(Boolean,default=True)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    room=relationship("Room",back_populates="location")
    
    # #route_from=relationship("Route",foreign_keys="Router.start_location_id",
    #                         back_populates="start_location",
    #                         cascade="all, delete-orphan")
    # #route_to=relationship("Route",foreign_keys="Router.end_location_id",
    #                       back_populates="start_location",
    #                       cascade="all, delete-orphan")