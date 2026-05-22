# Income Prediction Classification Project

## Overview
This project is an income classification application built using Python, machine learning, and web APIs. It predicts whether an individual earns more than $50K per year based on census-style features such as age, workclass, education, occupation, and hours worked per week.

The solution includes:
- `main.py`: FastAPI backend that loads a pre-trained classification model and exposes a `/predict` endpoint.
- `frontend.py`: Streamlit-based web interface for entering user attributes and requesting predictions.
- `Classification.ipynb`: Jupyter Notebook likely used for data exploration, model training, preprocessing, and evaluation.
- `adult.csv`: Dataset used for training or analysis, based on the UCI Adult Income dataset.
- `Dockerfile`: Container definition for running the backend in a consistent Python environment.
- `requirements.txt`: Python dependencies for both backend and frontend.

## Components

### Backend (`main.py`)
- Uses FastAPI to create a REST API.
- Loads a serialized model from `svc_model_3.pkl`.
- Accepts JSON input for features such as:
  - `age`
  - `workclass`
  - `education`
  - `marital_status`
  - `occupation`
  - `relationship`
  - `gender`
  - `capital_gain`
  - `capital_loss`
  - `hours_per_week`
  - `native_country`
- Returns a prediction indicating whether the income is expected to be `>50K` or `<=50K`.
- Live backend hosted on Hugging Face at `https://abdullahkamran426-income-predictor-backend.hf.space/predict`.

### Frontend (`frontend.py`)
- Uses Streamlit for a quick user interface.
- Collects user input for the same set of features.
- Sends a POST request to the backend prediction endpoint.
- Displays the prediction result or error details.
- Currently configured to send predictions to `https://abdullahkamran426-income-predictor-backend.hf.space/predict`.
- Live frontend deployed on Streamlit: https://income-predictor-zvrnvoeezsxuj85lfxygjc.streamlit.app/

### How it Works
1. The user opens the Streamlit interface and fills in the required income features.
2. When the user clicks `Predict`, the frontend sends a JSON POST request to the backend endpoint.
3. The backend `main.py` receives the request and validates the incoming data using Pydantic.
4. Backend converts the request into a pandas DataFrame and passes it into the trained model.
5. The model returns a prediction of whether the income is `>50K` or `<=50K`.
6. The backend returns the prediction as JSON, and the frontend displays the result to the user.

### Deployment
- The backend is live on Hugging Face at `https://abdullahkamran426-income-predictor-backend.hf.space/predict`.
- The frontend is live on Streamlit at `https://income-predictor-zvrnvoeezsxuj85lfxygjc.streamlit.app/`.

### Docker support
- `Dockerfile` installs Python dependencies and runs `main.py`.
- This allows the backend to be deployed as a containerized service.

## Dependencies
The project dependencies are listed in `requirements.txt`:
- `fastapi`
- `uvicorn`
- `pydantic`
- `pandas`
- `scikit-learn`

## Notes
- The backend requires the file `svc_model_3.pkl` to be present in the project root.
- If you want the frontend to use a local backend instead of the hosted URL, update the `requests.post(...)` URL in `frontend.py` to point at `http://127.0.0.1:7860/predict` or the appropriate local host and port.
- `Classification.ipynb` can be used to review how the model was trained, validated, and saved.

## Project Goals
- Build a complete ML inference pipeline from dataset to web app.
- Provide a simple UI for income prediction.
- Enable deployment through Docker and local execution via FastAPI and Streamlit.
