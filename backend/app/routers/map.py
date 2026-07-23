from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.models.location import Location
from app.core.database import get_db
from app.schemas.location import LocationResponse

router=APIRouter(prefix="/Map",tags=["Map"])

@router.get("/location",response_model=list[LocationResponse])
def get_locations(db:Session=Depends(get_db)):
    location=db.query(Location).all()
    
    return location
#[
    #     {
    #         "id":location.id,
    #         "room_id":location.room_id,
    #         "latitude":location.latitude,
    #         "longitude":location.longitude
    #     }
    #     for location in locations
    # ]