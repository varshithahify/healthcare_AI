# 💊 AI Healthcare Dashboard

A smart web-based healthcare application that predicts diabetes risk using Machine Learning and provides basic medical guidance.

---

## 🚀 Live Demo

👉 https://healthcareai-c6w7ehkjhpslyvgkzzpmmp.streamlit.app

---

## 📌 Features

* 🧠 **AI Disease Prediction**

  * Predicts diabetes risk using trained ML model
* 📊 **Interactive Dashboard**

  * Visual risk representation using gauge chart
* 🧑‍⚕️ **Patient Record Management**

  * Stores patient details in SQLite database
* 🤖 **AI Doctor Chatbot**

  * Provides basic health suggestions based on symptoms
* 🌐 **Deployed Online**

  * Accessible from anywhere using Streamlit Cloud

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **Machine Learning:** Scikit-learn
* **Database:** SQLite
* **Visualization:** Plotly

---

## 📂 Project Structure

```
healthcare_AI/
│
├── app.py              # Main Streamlit app
├── model.pkl           # Trained ML model
├── model.py            # Model training script
├── database.py         # Database setup
├── dataset.csv         # Dataset used for training
├── patients.db         # SQLite database
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
```

---

## ⚙️ Installation (Local Setup)

1. Clone the repository:

```
git clone https://github.com/varshithahify/healthcare_AI.git
cd healthcare_AI
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

---

## 📊 How It Works

1. User enters:

   * Age
   * Blood Pressure
   * Glucose Level

2. Model processes input → predicts diabetes risk

3. Output:

   * Risk percentage (Gauge chart)
   * High / Low risk message

---

## ⚠️ Disclaimer

This application is for **educational purposes only**.
It does **not replace professional medical advice**.

---

## 👩‍💻 Author

**Varshitha Varsha**
🔗 GitHub: https://github.com/varshithahify

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
