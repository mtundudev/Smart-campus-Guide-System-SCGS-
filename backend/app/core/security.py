from datetime import datetime,timedelta
from app.core.config import settings
from jose import jwt,JWTError
from app.models.user import User,RoleEnum
from app.core.database import get_db
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
import bcrypt

oauth2_schema=OAuth2PasswordBearer(tokenUrl="Auth/login")


def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.now()+timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    token=jwt.encode(to_encode,settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    return token

def decode_token(token:str):
    try:
        payload=jwt.decode(token,settings.SECRET_KEY,algorithms=[settings.ALGORITHM])
        return  payload
    except JWTError: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="token has no information")
    
def get_current_user(token:str=Depends(oauth2_schema),db:Session=Depends(get_db)):    
    payload=decode_token(token)
    user_id=payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="token has no required information")
    user=db.query(User).filter(User.id==int(user_id)).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="token has wrong user")
    if not user.is_active:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="account is not active")
    return user

def require_admin(current_user:User=Depends(get_current_user)):
    if current_user.role!=RoleEnum.admin:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="only admin can access this resource")
    return current_user

def require_admin_staff_or_student(current_user:User=Depends(get_current_user)):
    if current_user.role not in [RoleEnum.admin,RoleEnum.student,RoleEnum.staff]:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="only  authorized can access")
    return current_user

    
class Hash():
    def password_hash(password):
        pass_byte=password.encode("utf-8")
        salt_byte=bcrypt.gensalt()
        hashed=bcrypt.hashpw(pass_byte,salt_byte)
        return hashed.decode("utf-8")
    
    def password_verify(plain_password,hashed_password):
        plain_byte=plain_password.encode("utf-8")
        hashed_byte=hashed_password.encode("utf-8")
        return bcrypt.checkpw(plain_byte,hashed_byte)