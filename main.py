from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Restaurant-BERT Triage API")

MODEL_ID = "Belomoh66/Restaurant-BERT-Triage" 

print(f"Loading model from Hugging Face: {MODEL_ID}...")
# device=0 ensures it utilizes your local GPU
classifier = pipeline("text-classification", model=MODEL_ID, tokenizer=MODEL_ID, device=0)

class Query(BaseModel):
    text: str

@app.post("/classify")
async def classify_message(query: Query):
    prediction = classifier(query.text)[0]
    
    return {
        "status": "success",
        "intent": prediction["label"],
        "confidence": round(prediction["score"] * 100, 2)
    }

# Run command: uvicorn main:app --host 0.0.0.0 --port 8000
