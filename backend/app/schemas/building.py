from pydantic import BaseModel,field_validator
from datetime import datetime
from typing import Optional

class BuildingCreate(BaseModel):
    building_name:str
    building_code:str
    description:Optional[str]=None
    
class BuidingUpdate(BaseModel):
    building_name:Optional[str]=None
    building_code:Optional[str]=None
    description:Optional[str]=None
    
class BuidingResponse(BaseModel):
    id:int
    building_name:str
    building_code:Optional[str]=None
    description:Optional[str]=None    
    created_at:datetime
    updated_at:datetime
    
    @field_validator("building_name","building_code")
    @staticmethod
    def name_validator(cls,v):
        return v.upper()