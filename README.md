# 🏡 House Price Predictor (India)

This project is a **Machine Learning-powered web app** that predicts house prices in India based on user-input features like the number of bedrooms, bathrooms, living area size, condition, and nearby schools. It’s built with **Python**, **Scikit-learn**, and **Streamlit** for an interactive web interface.

---

## 🚀 Features

- 💡 **Machine Learning Model** trained on real-world housing data.  
- 🧠 **Predicts house prices** based on user inputs.  
- 🌐 **Streamlit Web App** for an easy and interactive user experience.  
- 🎈 Fun UI with animations (`st.balloons()` 🎈).  
- 💾 Pre-trained model stored as `model.pkl` using `joblib`.

---

## 🧩 Tech Stack

- Python 
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **Joblib**

---

## ⚙️ How It Works

1. **Data Preprocessing & Training**  
   The dataset (`House Price India.csv`) is cleaned, preprocessed, and used to train a regression model.

2. **Model Saving**  
   The trained model is saved using `joblib` as `model.pkl`.

3. **Web App (Streamlit)**  
   The app (`app.py`) loads the model and allows users to input house features through an interactive interface.

4. **Prediction**  
   The app displays a predicted price instantly upon clicking the “Predict!” button.

---

## 🧠 Example Inputs

| Feature | Example |
|----------|----------|
| Bedrooms | 3 |
| Bathrooms | 2 |
| Living Area | 1800 |
| Condition | 4 |
| Schools Nearby | 2 |

---

## 💰 Example Output

Price Prediction is: ₹ 8,750,000.00

---

📊 Future Improvements

- Add location-based features (city, zip code, etc.)
- Integrate data visualization dashboard
- Deploy app on Streamlit Cloud or Hugging Face Spaces
- Add model comparison and feature importance visualization

