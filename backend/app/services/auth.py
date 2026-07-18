from app.schemas.user import UserRegister
from sqlalchemy.orm import Session
from app.models.user import User
from fastapi import HTTPException,status
from app.core.security import Hash,create_access_token

def registeruser(data:UserRegister,db:Session):
    existing=db.query(User).filter(User.email==data.email).first()
    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"{data.email}. email already exist")
    hashed_password=Hash.password_hash(data.password)
    user=User(**data.model_dump())
    user.password=hashed_password
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def loginuser(email:str,password:str,db:Session):
    user=db.query(User).filter(User.email==email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="check your usename or email")
    hash_password=Hash.password_verify(password,user.password)
    if not hash_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="check your password")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="account is not active")
    access_token=create_access_token({"sub":str(user.id)})
    return{
        "access_token":access_token,
        "token_type":"Bearer"
    }         