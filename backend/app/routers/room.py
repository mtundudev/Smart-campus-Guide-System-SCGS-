from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.room import RoomCreate,RoomResponse,RoomUpdate
from app.services.room import create_room,show_all_room,show_room,Update_room_info,delete_room_info
router=APIRouter(tags=["Room Managment"],prefix="/Room")


@router.post("/create",response_model=RoomResponse)
def create(data:RoomCreate,db:Session=Depends(get_db)):
    return create_room(data,db)

@router.get("",response_model=list[RoomResponse])
def show_all(db:Session=Depends(get_db)):
    return show_all_room(db)
    

@router.get("/{id}",response_model=RoomResponse)
def show(id:int,db:Session=Depends(get_db)):
    return show_room(id,db)

@router.put("/{id}",response_model=RoomResponse)
def update_info(id:int,data:RoomUpdate,db:Session=Depends(get_db)):
    return Update_room_info(id,data,db)
        
@router.delete("/{id}")        
def delete(id:int,db:Session=Depends(get_db)):
    return delete_room_info(id,db)