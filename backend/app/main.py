from fastapi import FastAPI
from app.routers.user import router as user_router
from app.routers.auth import router as auth_router
from app.routers.building import router as building_router


app=FastAPI(title="SMART COMPUS GUIDE SYSTEM",description="location assistance")

from fastapi.staticfiles import StaticFiles
import os
if not os.path.exists("static"):
    os.makedirs("static")
    
app.mount("/static",StaticFiles(directory="static"),name="static")    

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(building_router)
