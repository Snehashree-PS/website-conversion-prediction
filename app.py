import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🛒 Website Conversion Prediction")

st.write("Enter values to predict")

# Inputs
page_values = st.number_input("Page Values")
exit_rate = st.number_input("Exit Rate")
bounce_rate = st.number_input("Bounce Rate")
product_related = st.number_input("Product Related")
duration = st.number_input("Product Related Duration")

# Button
if st.button("Predict"):
    input_data = pd.DataFrame(
        [[page_values, exit_rate, bounce_rate, product_related, duration]],
        columns=[
            "PageValues",
            "ExitRates",
            "BounceRates",
            "ProductRelated",
            "ProductRelated_Duration"
        ]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ User WILL Purchase")
    else:
        st.error("❌ User will NOT Purchase")