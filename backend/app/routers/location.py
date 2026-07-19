from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.location import LocationCreate,LocationResponse,LocationUpdate
from app.services.location import create_location,show_all_location,show_location,Update_location_info,delete_location_info

router=APIRouter(tags=["Location Managment"],prefix="/Location")


@router.post("/create",response_model=LocationResponse)
def create(data:LocationCreate,db:Session=Depends(get_db)):
    return create_location(data,db)

@router.get("",response_model=list[LocationResponse])
def show_all(db:Session=Depends(get_db)):
    return show_all_location(db)
    

@router.get("/{id}",response_model=LocationResponse)
def show(id:int,db:Session=Depends(get_db)):
    return show_location(id,db)

@router.put("/{id}",response_model=LocationResponse)
def update_info(id:int,data:LocationUpdate,db:Session=Depends(get_db)):
    return Update_location_info(id,data,db)
        
@router.delete("/{id}")        
def delete(id:int,db:Session=Depends(get_db)):
    return delete_location_info(id,db)