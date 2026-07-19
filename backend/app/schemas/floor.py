from pydantic import BaseModel,field_validator
from datetime import datetime
from typing import Optional
from app.schemas.building import BuidingResponse

class FloorCreate(BaseModel):
    floor_name:Optional[str]=None
    building_id:int
    
class FloorResponse(FloorCreate):
    id:int
    floor_number:Optional[int]=None
    created_at:datetime
    updated_at:datetime
    building:Optional[BuidingResponse]=None
    
    @field_validator("floor_name")
    @staticmethod
    def name_validator(cls,v):
        return v.upper()
    
class FloorUpdate(BaseModel):
    floor_name:Optional[str]=None
    floor_number:Optional[int]=None
    building_id:Optional[int]=None
    
    created_at:datetime
    update_at:datetime
   