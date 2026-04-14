from pydantic import BaseModel, Field
from datetime import datetime

class SensorData(BaseModel):
    temperature: float
    humidity: float
    pm25: float
    co: float
    co2: float
    ier: float | None = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)