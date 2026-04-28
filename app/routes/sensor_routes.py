from fastapi import APIRouter
from app.schemas.sensor_schema import SensorData
from app.services.sensor_service import create_sensor_data, get_all_sensors
from app.services.simulation_service import simulate_sensor

router = APIRouter(prefix="/sensor", tags=["Sensor Data"])

@router.post("/sensor")
async def add_sensor(data: SensorData):
    return await create_sensor_data(data)


@router.get("/sensor")
async def get_sensors():
    return await get_all_sensors()

@router.get("/simulate")
async def simulate():
    data = simulate_sensor()
    sensor = SensorData(**data)
    return await create_sensor_data(sensor)