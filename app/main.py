from fastapi import FastAPI
from app.routes import sensor_routes
from app.routes import auth_routes

app = FastAPI()

app.include_router(sensor_routes.router)

app.include_router(auth_routes.router)