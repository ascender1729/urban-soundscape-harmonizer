from fastapi import APIRouter, HTTPException
from ..models import SoundscapeData
from ..database import write_api, INFLUXDB_BUCKET, INFLUXDB_ORG
from influxdb_client import Point
import random

router = APIRouter()

@router.post("/soundscape")
async def record_soundscape(data: SoundscapeData):
    point = (
        Point("soundscape")
        .tag("location", data.location)
        .field("noise_level", data.noise_level)
        .field("frequency_distribution", str(data.frequency_distribution))
    )
    write_api.write(bucket=INFLUXDB_BUCKET, org=INFLUXDB_ORG, record=point)
    return {"message": "Soundscape data recorded successfully"}

@router.get("/soundscape/{location}")
async def get_soundscape(location: str):
    # Simulated data retrieval (replace with actual InfluxDB query in production)
    noise_level = random.uniform(30, 90)
    frequency_distribution = [random.uniform(0, 1) for _ in range(10)]
    return {
        "location": location,
        "noise_level": noise_level,
        "frequency_distribution": frequency_distribution
    }
