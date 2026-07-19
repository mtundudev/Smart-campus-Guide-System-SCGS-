from pydantic import BaseModel,field_validator
from datetime import datetime
from typing import Optional
from app.schemas.floor import FloorResponse

class RoomCreate(BaseModel):
    room_name:Optional[str]=None
    room_number:Optional[int]=None
    capacity:Optional[int]=None
    room_type:Optional[str]=None
    floor_id:Optional[int]=None
    
class RoomResponse(BaseModel):
    id:int
    room_name:Optional[str]=None
    room_number:Optional[int]=None
    capacity:Optional[int]=None
    room_type:Optional[str]=None
    floor_id:Optional[int]=None
    created_at:datetime
    updated_at:datetime
    floor:Optional[FloorResponse]=None
    
    @field_validator("room_name")
    @staticmethod
    def name_validator(cls,v):
        return v.upper()
    
    
class RoomUpdate(BaseModel):
    room_name:Optional[str]=None
    room_number:Optional[int]=None
    floor_id:Optional[int]=None
    capacity:Optional[int]=None
    room_type:Optional[str]=None
    
   