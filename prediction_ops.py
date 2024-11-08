# prediction_ops.py
from sklearn.linear_model import LinearRegression
import numpy as np

# Function to predict future mood trends
def predict_mood_trend(data, weeks_ahead=4):
    # Extract session numbers and mood scores for regression
    session_numbers = np.array(range(1, len(data) + 1)).reshape(-1, 1)
    mood_scores = np.array([row[3] for row in data]).reshape(-1, 1)
    
    # Train the linear regression model
    model = LinearRegression()
    model.fit(session_numbers, mood_scores)
    
    # Generate future session numbers
    future_sessions = np.array(range(len(data) + 1, len(data) + weeks_ahead + 1)).reshape(-1, 1)
    predictions = model.predict(future_sessions)
    
    # Convert predictions to a flat list for easier usage
    return predictions.flatten().tolist()

# Function to predict future stress trends (similar to mood trend function)
def predict_stress_trend(data, weeks_ahead=4):
    session_numbers = np.array(range(1, len(data) + 1)).reshape(-1, 1)
    stress_scores = np.array([row[4] for row in data]).reshape(-1, 1)
    
    model = LinearRegression()
    model.fit(session_numbers, stress_scores)
    
    future_sessions = np.array(range(len(data) + 1, len(data) + weeks_ahead + 1)).reshape(-1, 1)
    predictions = model.predict(future_sessions)
    
    return predictions.flatten().tolist()