from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal
import random

app = FastAPI()

# Dummy response, bisa dihubungkan dengan LSTM model nanti
class PredictionRequest(BaseModel):
    timeframe: Literal["1m", "5m", "1h", "1d"]

@app.get("/api/price")
def get_status():
    return {"message": "XAUUSD AI backend is running!"}

@app.post("/api/predict")
def predict_direction(request: PredictionRequest):
    # Ganti bagian ini nanti dengan model LSTM kamu
    result = random.choice(["buy", "sell", "hold"])
    return {"prediction": result, "timeframe": request.timeframe}

@app.get("/api/news")
def get_news():
    # Dummy news - nanti bisa fetch dari NewsAPI
    return {
        "news": [
            {"title": "Fed Raises Rates Again", "impact": "high"},
            {"title": "Gold Prices Volatile Amid Global Tensions", "impact": "medium"}
        ]
    }
