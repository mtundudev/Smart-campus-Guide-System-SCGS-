from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime
from app.schemas.room import RoomResponse

class LocationCreate(BaseModel):
    room_id:Optional[int]=None
    latitude:float=Field(ge=-90,le=90)
    longitude:float=Field(ge=-180,le=180)
   
    
class LocationResponse(LocationCreate):
    id:int
    is_accessible:bool
    indoor:bool
    created_at:datetime
    updated_at:datetime
    room:Optional[RoomResponse]=None
    
class LocationUpdate(BaseModel):
    room_id:Optional[int]=None
    latitude:Optional[float]=Field(ge=-90,le=90)
    longitude:Optional[float]=Field(ge=-180,le=180)