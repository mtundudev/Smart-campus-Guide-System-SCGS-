from fastapi import APIRouter,Depends, HTTPException,status,File,UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth import registeruser,loginuser
from app.services.user import showuser,deleteuser
from app.models.user import User
from app.schemas.user import UserResponse,UserUpdate
from sqlalchemy.orm import Session
from app.core.database import get_db
import os
from app.core.security import require_admin_staff_or_student,get_current_user,Hash,require_admin

router=APIRouter(prefix="/User",tags=["User Managment"])

@router.get("/me",response_model=UserResponse)
def my_profile(current_user=Depends(require_admin_staff_or_student)):
    return current_user

@router.get("/",response_model=list[UserResponse])
def show_all(db:Session=Depends(get_db),current_user=Depends(require_admin)):
    return showuser(db)

@router.put("/me",response_model=UserResponse)
def update_profile(data:UserUpdate,current_user:User=Depends(get_current_user),
                   db:Session=Depends(get_db)):
    current_user.full_name=data.full_name
    current_user.email=data.email
    
    db.commit()
    db.refresh(current_user)
    return current_user

@router.put("/password",response_model=UserResponse)
def my_password(current_password:str,new_password:str,
                db:Session=Depends(get_db),
                current_user:User=Depends(get_current_user)):
    if not Hash.password_verify(current_password,current_user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail= "wrong current password")
    current_user.password=Hash.password_hash(new_password)
    db.commit()
    db.refresh(current_user)
    return current_user

@router.delete("/me")
def my_profile(current_user:User=Depends(require_admin_staff_or_student),
               db:Session=Depends(get_db)):
    db.delete(current_user)
    db.commit()
    return {"message":"your account successfull deleted"}

@router.delete("/{id}")
def delete_user(id:int,db:Session=Depends(get_db)):
    return deleteuser(id,db)

@router.post("/me/upload_image")
def upload_profile(
    file:UploadFile=File(),
    db:Session=Depends(get_db),current_user:User=Depends(get_current_user) ):
    upload_dir="static/profile-pics"
    os.makedirs(upload_dir, exist_ok=True)
    
    file_path=f"{upload_dir}/user_{current_user.id}.png"
    
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
     
    current_user.profile_picture=f"{file_path}"
    db.commit() 
    db.refresh(current_user)
        
    return {"message":"CONGRATURATION",
            "path":file_path}    
