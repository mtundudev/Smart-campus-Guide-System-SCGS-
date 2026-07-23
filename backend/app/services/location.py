from app.schemas.location import LocationCreate,LocationUpdate
from sqlalchemy.orm import Session
from app.models.room import Room
from app.models.location import Location
from fastapi import HTTPException,status


def create_location(data:LocationCreate,db:Session):
    room=db.query(Room).filter(Room.id==data.room_id).first()
    if not room:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="targeted room not found ")
    location=Location(
        longitude=data.longitude,
        latitude=data.latitude,
        room_id=data.room_id
    )
    db.add(location)
    db.commit()
    db.refresh(location)
    return location

def show_all_location(db:Session):
    location=db.query(Location).all()
    return location

def show_location(id:int,db:Session):
    location=db.query(Location).filter(Location.id==id).first()
    if  not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the location with id {id} not found")
    return location

def Update_location_info(id:int,data:LocationUpdate,db:Session):
    location=db.query(Location).filter(Location.id==id).first()
    if  not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f" the location with id {id} not found")
    location.room_id=data.room_id
    location.latitude=data.latitude
    location.longitude=data.longitude
    
    db.commit()
    db.refresh(location)
    
    return location

def delete_location_info(id:int,db:Session):
    location=db.query(Location).filter(Location.id==id).delete(synchronize_session=False)
    if  not location:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"location with {id}  not found")
    db.commit()
    return {"message":"location information successful daleted"}