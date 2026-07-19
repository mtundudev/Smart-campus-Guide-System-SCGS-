from app.schemas.building import BuildingCreate,BuidingUpdate
from sqlalchemy.orm import Session
from app.models.building import Building
from fastapi import HTTPException,status



def create_building(data:BuildingCreate,db:Session):
    existing=db.query(Building).filter(Building.building_name==data.building_name).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="building already exist")
    building=Building(**data.model_dump())
    db.add(building)
    db.commit()
    db.refresh(building)
    return building

def show_all_buildings(db:Session):
    building=db.query(Building).all()
    return building

def show_building(id:int,db:Session):
    building=db.query(Building).filter(Building.id==id).first()
    if  not building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the building with id {id} not found")
    return building

def Update_buiding_info(id:int,data:BuidingUpdate,db:Session):
    building=db.query(Building).filter(Building.id==id).first()
    if  not building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f" the building with id {id} not found")
    building.buildung_name=data.building_name
    building.buildung_code=data.building_code
    building.description=data.description
    
    db.commit()
    db.refresh(building)
    return building

def delete_building_info(id:int,db:Session):
    building=db.query(Building).filter(Building.id==id).delete(synchronize_session=False)
    if  not building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"buildind with {id}  not found")
    return {"message":"building information successful daleted"}