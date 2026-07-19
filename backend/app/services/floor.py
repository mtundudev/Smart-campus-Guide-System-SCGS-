from app.schemas.floor import FloorCreate,FloorUpdate
from sqlalchemy.orm import Session
from app.models.floor import Floor
from app.models.building import Building
from fastapi import HTTPException,status



def create_floor(data:FloorCreate,db:Session):
    existing=db.query(Floor).filter(Floor.floor_name==data.floor_name).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="room name already created")
    building=db.query(Building).filter(Building.id==data.building_id).first()
    if not building:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="targeted building not found")
    floor=Floor(**data.model_dump())
    last_floor=db.query(Floor).order_by(Floor.id.desc()).first()
    if last_floor:
        floor.floor_number=last_floor.floor_number+1
    else:
        floor.floor_number=0    
    db.add(floor)
    db.commit()
    db.refresh(floor)
    return floor

def show_all_floor(db:Session):
    floor=db.query(Floor).all()
    return floor

def showfloor(id:int,db:Session):
    floor=db.query(Floor).filter(Floor.id==id).first()
    if  not floor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the floor with id {id} not found")
    return floor

def Update_floor_info(id:int,data:FloorUpdate,db:Session):
    floor=db.query(Floor).filter(Floor.id==id).first()
    if  not floor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f" the building with id {id} not found")
    floor.buildung_name=data.building_name
    floor.buildung_code=data.building_code
    floor.description=data.description
    
    db.commit()
    db.refresh(floor)
    return floor

def delete_floor_info(id:int,db:Session):
    floor=db.query(Floor).filter(Floor.id==id).delete(synchronize_session=False)
    if  not floor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"floor  with {id}  not found")
    db.commit()
    return {"message":"floor information successful daleted"}