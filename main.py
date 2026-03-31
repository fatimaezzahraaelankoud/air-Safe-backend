from fastapi import FastAPI
from routes.sensor_routes import router as sensor_router

app = FastAPI(title="AirSafe AI - Backend")

app.include_router(sensor_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'API AirSafe AI"}