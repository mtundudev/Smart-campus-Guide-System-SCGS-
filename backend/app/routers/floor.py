from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.floor import FloorCreate,FloorResponse,FloorUpdate
from app.services.floor import create_floor,show_all_floor,showfloor,Update_floor_info,delete_floor_info
router=APIRouter(tags=["Floor Managment"],prefix="/Floor")


@router.post("/create",response_model=FloorResponse)
def create(data:FloorCreate,db:Session=Depends(get_db)):
    return create_floor(data,db)

@router.get("",response_model=list[FloorResponse])
def show_all(db:Session=Depends(get_db)):
    return show_all_floor(db)
    

@router.get("/{id}",response_model=FloorResponse)
def show(id:int,db:Session=Depends(get_db)):
    return showfloor(id,db)

@router.put("/{id}",response_model=FloorResponse)
def update_info(id:int,data:FloorUpdate,db:Session=Depends(get_db)):
    return Update_floor_info(id,data,db)
        
@router.delete("/{id}")        
def delete(id:int,db:Session=Depends(get_db)):
    return delete_floor_info(id,db)