from app.core.database import Base
from sqlalchemy import Column,Integer,String,DateTime,Enum,Boolean,ForeignKey,Float
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

class Route(Base):
    __tablename__="routes"
    id=Column(Integer,primary_key=True,index=True)
    start_location_id=Column(Integer,ForeignKey("locations.id",ondelete="CASCADE"),nullable=False)
    end_location_id=Column(Integer,ForeignKey("locations.id",ondelete="CASCADE"),nullable=False)
    distance=Column(Float,nullable=False)
    estimated_time=Column(Integer,nullable=False)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    
    start_location=relationship("Location",back_populates="route_from",foreign_keys=[start_location_id])
    end_location=relationship("Location",back_populates="route_to",foreign_keys=[end_location_id])
    