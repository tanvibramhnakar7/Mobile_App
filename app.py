import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("best_model.pkl", "rb"))

# Streamlit App
st.set_page_config(page_title="📱 Mobile Price Range Predictor", layout="centered")

st.title("📱 Mobile Price Range Prediction App")
st.write("Predict the price range (0: Low, 1: Medium, 2: High, 3: Very High) based on mobile specifications.")

st.header("Enter Mobile Features")

# Input fields for each feature
battery_power = st.number_input("Battery Power (mAh)", min_value=500, max_value=5000, value=1500)
blue = st.selectbox("Bluetooth", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
clock_speed = st.number_input("Clock Speed (GHz)", min_value=0.5, max_value=3.0, value=1.8)
dual_sim = st.selectbox("Dual SIM", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
fc = st.number_input("Front Camera (MP)", min_value=0, max_value=20, value=5)
four_g = st.selectbox("4G Support", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
int_memory = st.number_input("Internal Memory (GB)", min_value=2, max_value=256, value=32)
m_dep = st.number_input("Mobile Depth (cm)", min_value=0.1, max_value=1.0, value=0.5)
mobile_wt = st.number_input("Mobile Weight (grams)", min_value=50, max_value=250, value=150)
n_cores = st.slider("Number of Cores", 1, 8, 4)
pc = st.number_input("Primary Camera (MP)", min_value=0, max_value=30, value=12)
px_height = st.number_input("Pixel Height", min_value=500, max_value=2000, value=1200)
px_width = st.number_input("Pixel Width", min_value=500, max_value=2000, value=800)
ram = st.number_input("RAM (MB)", min_value=256, max_value=8000, value=4000)
sc_h = st.slider("Screen Height (cm)", 5, 20, 10)
sc_w = st.slider("Screen Width (cm)", 2, 10, 5)
talk_time = st.number_input("Talk Time (hours)", min_value=2, max_value=30, value=10)
three_g = st.selectbox("3G Support", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
touch_screen = st.selectbox("Touch Screen", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")
wifi = st.selectbox("WiFi", [0, 1], format_func=lambda x: "Yes" if x==1 else "No")

# Create feature array
features = np.array([[battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, 
                      m_dep, mobile_wt, n_cores, pc, px_height, px_width, ram, 
                      sc_h, sc_w, talk_time, three_g, touch_screen, wifi]])

# Predict button
if st.button("Predict Price Range"):
    prediction = model.predict(features)[0]
    ranges = {0: "Low Cost 💸", 1: "Medium Cost 💰", 2: "High Cost 💎", 3: "Very High Cost 🚀"}
    st.success(f"### 📊 Predicted Price Range: {ranges[prediction]}")
