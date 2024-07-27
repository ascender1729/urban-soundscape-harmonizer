from fastapi import APIRouter, HTTPException
from ..models import SoundscapeData
from ..database import write_api, INFLUXDB_BUCKET, INFLUXDB_ORG
from influxdb_client import Point

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
