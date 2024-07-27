from pydantic import BaseModel
from typing import List

class SoundscapeData(BaseModel):
    location: str
    noise_level: float
    frequency_distribution: List[float]
    timestamp: str
