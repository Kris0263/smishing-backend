
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

class SMSInput(BaseModel):
    message: str

app = FastAPI()

@app.post("/predict")
def predict_sms(input_data: SMSInput):
    try:
        text_vector = vectorizer.transform([input_data.message])
        prediction = model.predict(text_vector)[0]
        label = "smishing" if prediction == 1 else "ham"
        return {"prediction": int(prediction), "label": label}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
