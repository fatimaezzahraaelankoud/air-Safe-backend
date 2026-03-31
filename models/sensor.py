from pydantic import BaseModel
from datetime import datetime


class SensorData(BaseModel):
    temperature: float
    humidity: float
    pm25: float
    co: float
    co2: float
    ier: float
    timestamp: datetime = datetime.now()