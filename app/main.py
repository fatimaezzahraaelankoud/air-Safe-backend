from fastapi import FastAPI
from app.routes import sensor_routes

app = FastAPI()

app.include_router(sensor_routes.router)