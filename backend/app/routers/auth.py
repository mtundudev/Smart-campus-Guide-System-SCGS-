from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.services.auth import registeruser,loginuser
from app.schemas.user import UserRegister,UserResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import require_admin_staff_or_student,get_current_user

router=APIRouter(prefix="/Auth",tags=["Authentication"])

@router.post("/",response_model=UserResponse,summary="register a new user")
def register(data:UserRegister,db:Session=Depends(get_db)):
    return registeruser(data,db)

@router.post("/login")
def login(data:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    return loginuser(data.username,data.password,db)

@router.get("/me",response_model=UserResponse)
def my_profile(current_user=Depends(require_admin_staff_or_student)):
    return current_user

