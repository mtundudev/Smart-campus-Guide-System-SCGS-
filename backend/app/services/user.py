from app.models.user import User
from sqlalchemy.orm import Session
from fastapi import HTTPException,status


def showuser(db:Session):
    user=db.query(User).all()
    return user 

def deleteuser(id:int,db:Session):
    user=db.query(User).filter(User.id==id).delete(synchronize_session=False)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    db.commit()
    return{"message":"deleted successfully"}