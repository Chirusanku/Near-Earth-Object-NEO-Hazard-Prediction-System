import streamlit as st
import pandas as pd
import joblib

# Load the model using a relative path
# Ensure you save your best model as 'model.pkl' in the same folder on GitHub
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

try:
    model = load_model()
except FileNotFoundError:
    st.error("Model file 'model.pkl' not found. Please upload it to your GitHub repository.")
    st.stop()

st.set_page_config(page_title="NEO Hazard Predictor", page_icon="☄️", layout="centered")

st.title("☄️ Near-Earth Object (NEO) Hazard Predictor")
st.markdown("**Developed by:** CHIRU | **Batch No.** 465")
st.markdown("---")

st.write("Enter the asteroid's measurements below to predict if it is hazardous:")

# Form for user inputs
with st.form("neo_form"):
    
    # Input fields
    est_diameter_min = st.number_input("Estimated Diameter Min (km)", value=0.1, format="%.4f")
    est_diameter_max = st.number_input("Estimated Diameter Max (km)", value=0.2, format="%.4f")
    relative_velocity = st.number_input("Relative Velocity (km/h)", value=50000.0, format="%.2f")
    miss_distance = st.number_input("Miss Distance (km)", value=5000000.0, format="%.2f")
    absolute_magnitude = st.number_input("Absolute Magnitude (H)", value=20.0, format="%.4f")

    submit_button = st.form_submit_button(label="Predict Hazard")

if submit_button:
    # IMPORTANT: Exact names and exact order expected by the model
    input_data = pd.DataFrame({
        "est_diameter_min": [est_diameter_min],
        "est_diameter_max": [est_diameter_max],
        "relative_velocity": [relative_velocity],
        "miss_distance": [miss_distance],
        "absolute_magnitude": [absolute_magnitude]
    })

    try:
        # The pipeline automatically handles the scaling (MinMax/Standard)
        prediction = model.predict(input_data)[0]
        
        if prediction == 1:
            st.error("⚠️ **Hazardous**: This Near-Earth Object poses a potential threat.")
        else:
            st.success("✅ **Non-Hazardous**: This object is not considered a threat.")
            
    except ValueError as e:
        st.error("Prediction Error: Feature mismatch.")
        st.info(f"Details: {e}")
