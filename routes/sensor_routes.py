from fastapi import APIRouter
from models.sensor import SensorData

router = APIRouter()

#  Route post pour recevoir les données 
@router.post("/sensor-data")
async def receive_data(data: SensorData):
    # Pour l'instant, on affiche juste dans le terminal
    print(f"--- Données Reçues ---")
    print(f"Temp: {data.temperature}°C | Humidity: {data.humidity} | PM2.5: {data.pm25} | CO: {data.co} | CO2: {data.co2} | IER: {data.ier} | Timestamp: {data.timestamp} ")
    return {"status": "success", "received": data}

