import streamlit as st
import sqlite3
import numpy as np
import pickle
import plotly.graph_objects as go

# ---------------- LOAD MODEL ----------------

model = pickle.load(open("model.pkl", "rb"))

# ---------------- DATABASE ----------------
conn = sqlite3.connect("patients.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS patients (
    name TEXT,
    age INTEGER,
    bp INTEGER,
    sugar INTEGER
)
""")

conn.commit()
conn.close()

# ---------------- UI STYLE ----------------

st.set_page_config(page_title="AI Healthcare Dashboard", layout="wide")

st.markdown("""

<style>
.main {
    background-color: #0e1117;
}
</style>

""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------

menu = st.sidebar.selectbox("Menu", ["Home", "Predict", "Patients", "Chatbot"])

# ---------------- HOME ----------------

if menu == "Home":
    st.title("💊 AI Healthcare Dashboard")
    st.subheader("Smart Disease Prediction System")
    st.write("This AI system predicts diabetes risk.")

# ---------------- PREDICT ----------------

elif menu == "Predict":

    st.header("🧠 Predict Health Risk")

    name = st.text_input("Enter Patient Name")
    age = st.slider("Age", 1, 100)
    bp = st.slider("Blood Pressure", 50, 180)
    sugar = st.slider("Glucose Level", 50, 200)

    if st.button("Predict Risk"):

        input_data = np.array([[0, sugar, bp, 0, 0, 0, 0, 0]])

        prediction = model.predict(input_data)
        prob = model.predict_proba(input_data)[0][1]

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prob * 100,
            title={'text': "Diabetes Risk %"},
            gauge={'axis': {'range': [0, 100]}}
        ))

        st.plotly_chart(fig)

        if prediction[0] == 1:
            st.error("⚠ High Risk of Diabetes")
        else:
            st.success("✅ Low Risk")

        conn = sqlite3.connect("patients.db")
        c = conn.cursor()

        c.execute(
            "INSERT INTO patients (name, age, bp, sugar) VALUES (?, ?, ?, ?)",
            (name, age, bp, sugar)
        )

        conn.commit()
        conn.close()

        st.success("Patient saved!")

    # Gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prob * 100,
        title={'text': "Diabetes Risk %"},
        gauge={'axis': {'range': [0, 100]}}
    ))

    st.plotly_chart(fig)

    if prediction[0] == 1:
        st.error("⚠ High Risk of Diabetes")
    else:
        st.success("✅ Low Risk")

    # Save to database
    conn = sqlite3.connect("patients.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO patients (name, age, bp, sugar) VALUES (?, ?, ?, ?)",
        (name, age, bp, sugar)
    )

    conn.commit()
    conn.close()

    st.success("Patient saved successfully!")


# ---------------- PATIENTS ----------------
# ---------------- PATIENTS ----------------
elif menu == "Patients":

    st.header("📋 Patient Records")

    conn = sqlite3.connect("patients.db")
    c = conn.cursor()

    data = c.execute("SELECT * FROM patients").fetchall()
    conn.close()

    st.write(data)


# ---------------- CHATBOT ----------------
elif menu == "Chatbot":

    st.header("🤖 AI Doctor Assistant")

    symptoms = st.text_input("Describe your symptoms (e.g., fever, cold)")

    if st.button("Get Advice"):

        symptoms = symptoms.lower()

        if "fever" in symptoms:
            st.warning("You may have an infection. Stay hydrated and consult a doctor.")
        elif "cold" in symptoms:
            st.info("It might be a common cold. Rest and drink warm fluids.")
        elif "headache" in symptoms:
            st.info("Take rest and stay hydrated. If persistent, consult a doctor.")
        else:
            st.success("Please consult a healthcare professional for accurate diagnosis.")


# ---------------- CHATBOT ----------------

elif menu == "Chatbot":

    st.header("🤖 AI Doctor Assistant")

    symptoms = st.text_input("Describe your symptoms (e.g., fever, cold)")

    if st.button("Get Advice"):

        symptoms = symptoms.lower()

        if "fever" in symptoms:
            st.warning("You may have an infection. Stay hydrated and consult a doctor.")
        elif "cold" in symptoms:
            st.info("It might be a common cold. Rest and drink warm fluids.")
        elif "headache" in symptoms:
            st.info("Take rest and stay hydrated. If persistent, consult a doctor.")
        else:
            st.success("Please consult a healthcare professional for accurate diagnosis.")