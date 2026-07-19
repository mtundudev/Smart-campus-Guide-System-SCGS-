from app.schemas.room import RoomCreate,RoomUpdate
from sqlalchemy.orm import Session
from app.models.floor import Floor
from app.models.room import Room
from fastapi import HTTPException,status



def create_room(data:RoomCreate,db:Session):
    existing=db.query(Room).filter(Room.room_name==data.room_name).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_208_ALREADY_REPORTED,detail="room name already exist")
    floor=db.query(Floor).filter(Floor.id==data.floor_id).first()
    if not floor:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="targeted floor not found ")
    room=Room(**data.model_dump())
    db.add(room)
    db.commit()
    db.refresh(room)
    return room

def show_all_room(db:Session):
    room=db.query(Room).all()
    return room

def show_room(id:int,db:Session):
    room=db.query(Room).filter(Room.id==id).first()
    if  not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the room with id {id} not found")
    return room

def Update_room_info(id:int,data:RoomUpdate,db:Session):
    room=db.query(Room).filter(Room.id==id).first()
    if  not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f" the room with id {id} not found")
    room.room_name=data.room_name
    room.room_number_code=data.room_number
    room.floor_id=data.floor_id
    room.capacity=data.capacity
    room.room_type=data.room_type
    
    db.commit()
    db.refresh(room)
    return room

def delete_room_info(id:int,db:Session):
    room=db.query(Room).filter(Room.id==id).delete(synchronize_session=False)
    if  not room:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"room with {id}  not found")
    return {"message":"room information successful daleted"}