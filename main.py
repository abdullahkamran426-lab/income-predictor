import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel  # Added this import

app = FastAPI()

# 1. Define the incoming JSON structure
class PredictionInput(BaseModel):
    age: int
    workclass: str
    education: str
    marital_status: str
    occupation: str
    relationship: str
    gender: str
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    native_country: str

with open("svc_model_3.pkl", "rb") as f:
    model = pickle.load(f)

@app.post("/predict")
def predict(data: PredictionInput):  # Changed parameters to use the Pydantic model
    # Map model variables by accessing them from the 'data' object
    data_dict = {
        "age": [data.age],
        "workclass": [data.workclass.strip()],
        "education": [data.education.strip()],
        "marital-status": [data.marital_status.strip()],
        "occupation": [data.occupation.strip()],
        "relationship": [data.relationship.strip()],
        "gender": [data.gender.strip()],
        "capital-gain": [data.capital_gain],
        "capital-loss": [data.capital_loss],
        "hours-per-week": [data.hours_per_week],
        "native-country": [data.native_country.strip()]
    }

    df = pd.DataFrame(data_dict)

    # Get the raw string prediction from your pipeline
    prediction = model.predict(df)[0]
    
    return {"prediction": str(prediction)}
