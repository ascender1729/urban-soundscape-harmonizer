from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import random
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SoundscapeData(BaseModel):
    location: str
    noise_level: float
    frequency_distribution: List[float]
    timestamp: float

@app.get("/")
async def root():
    return {"message": "Welcome to Urban Soundscape Harmonizer"}

@app.post("/soundscape")
async def create_soundscape(data: SoundscapeData):
    try:
        print(f"Received data for {data.location}: Noise level {data.noise_level}")
        return {"message": "Soundscape data recorded successfully"}
    except Exception as e:
        print(f"Error in create_soundscape: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/soundscape/{location}")
async def get_soundscape(location: str):
    try:
        noise_level = random.uniform(30, 90)
        frequency_distribution = [random.uniform(0, 1) for _ in range(10)]
        timestamp = time.time()

        data = SoundscapeData(
            location=location,
            noise_level=noise_level,
            frequency_distribution=frequency_distribution,
            timestamp=timestamp
        )

        return data
    except Exception as e:
        print(f"Error in get_soundscape: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3001)