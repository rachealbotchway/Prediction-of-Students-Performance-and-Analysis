# Import the necessary libraries
from fastapi import FastAPI
import pickle
import pandas as pd



# Create a new FastAPI app instance
app = FastAPI()

# Load the trained model from a pickle file
with open("student_performance_model.pkl", "rb") as file:
    model = pickle.load(file)

# Define a POST route for making predictions
@app.post("/predict")
async def predict_performance(df: dict):
    # Convert the input data to a pandas DataFrame
    df = pd.DataFrame([df])
    
    # Use the loaded model to make a prediction
    prediction = model.predict(df)[0]
    
    # Return the prediction result as a JSON object
    return {"predicted_math_score": prediction}






