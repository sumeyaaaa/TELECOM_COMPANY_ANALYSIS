import streamlit as st
import pandas as pd
from sklearn.pipeline import Pipeline
import joblib

# Load the trained model
pipeline = joblib.load('random_forest_model.pkl')

# Set the known minimum and maximum scores (replace these with your actual values)
min_score = 0  # example minimum score
max_score = 10  # example maximum score

# Set up the Streamlit app
st.title("Satisfaction Score Prediction")

# Create input fields for the features
features = {
    'Avg RTT DL (ms)': st.number_input('Avg RTT DL (ms)', format="%.2f"),
    'Avg RTT UL (ms)': st.number_input('Avg RTT UL (ms)', format="%.2f"),
    'Avg Bearer TP DL (kbps)': st.number_input('Avg Bearer TP DL (kbps)', format="%.2f"),
    'Avg Bearer TP UL (kbps)': st.number_input('Avg Bearer TP UL (kbps)', format="%.2f"),
    'TCP DL Retrans. Vol (Bytes)': st.number_input('TCP DL Retrans. Vol (Bytes)', format="%.2f"),
    'TCP UL Retrans. Vol (Bytes)': st.number_input('TCP UL Retrans. Vol (Bytes)', format="%.2f"),
    'Activity Duration DL (ms)': st.number_input('Activity Duration DL (ms)', format="%.2f"),
    'Activity Duration UL (ms)': st.number_input('Activity Duration UL (ms)', format="%.2f"),
    'Total DL (Bytes)': st.number_input('Total DL (Bytes)', format="%.2f"),
    'Total UL (Bytes)': st.number_input('Total UL (Bytes)', format="%.2f"),
}



# Button for prediction
if st.button('Predict Satisfaction Score'):
    input_data = pd.DataFrame([features])
    prediction = pipeline.predict(input_data)[0]
    
    # Normalize the prediction to a percentage
    predicted_percentage = (prediction - min_score) / (max_score - min_score) * 100

    # Ensure the value is clamped between 0 and 100
    predicted_percentage = max(0, min(predicted_percentage, 100))

    st.write(f"Predicted Satisfaction Score: {predicted_percentage:.2f}%")
