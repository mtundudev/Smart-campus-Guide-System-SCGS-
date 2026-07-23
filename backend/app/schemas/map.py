from pydantic import BaseModel

class MapResponse(BaseModel):
    id:int
    roon_id:int
    latitude:float
    longitude:float