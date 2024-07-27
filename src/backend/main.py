from fastapi import FastAPI
from .routers import soundscape

app = FastAPI(title="Urban Soundscape Harmonizer")

app.include_router(soundscape.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Urban Soundscape Harmonizer"}
