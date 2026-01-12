📱 Mobile Price Range Prediction App:
This project is a Streamlit web application designed to predict the price range of mobile phones based on their specifications.
The model classifies mobiles into four categories:
0 → Low Cost 💸
1 → Medium Cost 💰
2 → High Cost 💎
3 → Very High Cost 🚀
The app takes various mobile features as input and uses a trained machine learning model (best_ml.pkl) to generate predictions.

🚀 Features:
User-friendly Streamlit UI
Takes 20 mobile features as input
Predicts the price range instantly
Clean and intuitive sliders, dropdowns, and number input fields

🧠 Machine Learning Model:
The model is pre-trained and stored in best_ml.pkl
It expects the following features in the exact order:
['battery_power', 'blue', 'clock_speed', 'dual_sim', 'fc', 'four_g',
 'int_memory', 'm_dep', 'mobile_wt', 'n_cores', 'pc', 'px_height',
 'px_width', 'ram', 'sc_h', 'sc_w', 'talk_time', 'three_g',
 'touch_screen', 'wifi']

🧪 Technologies Used:
Python
Streamlit
NumPy
Pickle
Machine Learning (Classification Models)

📊 How the Prediction Works:
User enters mobile specifications
Input values are converted into a NumPy array
The trained model predicts the price category
The prediction is displayed with icons & labels

📝 Example Output:
📊 Predicted Price Range: High Cost 💎

🙌 Author:
Tanvi Bramhnakar
(You can add your email, GitHub, or LinkedIn here)
