from fastapi import FastAPI
from app.routers.user import router as user_router


app=FastAPI(title="SMART COMPUS GUIDE SYSTEM",description="location assistance")

app.include_router(user_router)