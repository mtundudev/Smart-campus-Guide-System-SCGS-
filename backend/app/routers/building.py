from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.building import BuildingCreate,BuidingUpdate,BuidingResponse
from app.services.buildings import create_building,show_all_buildings,delete_building_info,Update_buiding_info,show_building
router=APIRouter(tags=["Building Managment"],prefix="/Building")


@router.post("/create",response_model=BuidingResponse)
def create(data:BuildingCreate,db:Session=Depends(get_db)):
    return create_building(data,db)

@router.get("",response_model=list[BuidingResponse])
def show_all(db:Session=Depends(get_db)):
    return show_all_buildings(db)
    

@router.get("/{id}",response_model=BuidingResponse)
def show(id:int,db:Session=Depends(get_db)):
    return show_building(id,db)

@router.put("/{id}",response_model=BuidingResponse)
def update_info(id:int,data:BuidingUpdate,db:Session=Depends(get_db)):
    return Update_buiding_info(id,data,db)
        
@router.delete("/{id}")        
def delete(id:int,db:Session=Depends(get_db)):
    return delete_building_info(id,db)