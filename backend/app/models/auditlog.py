from app.core.database import Base
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Audit_log(Base):
    __tablename__="audits"
    
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    action=Column(String,nullable=False)
    resource=Column(String,nullable=False)
    ip_address=Column(String,nullable=False)
    
    created_at=Column(DateTime,default=datetime.now)
    updated_at=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    user=relationship("User",back_populates="audit")
    
    