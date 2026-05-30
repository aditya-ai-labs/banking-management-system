import streamlit as st
import requests

st.title("💰 Deposit Money")

customer_id = st.number_input(
    "Customer ID",
    min_value=1
)

amount = st.number_input(
    "Deposit Amount",
    min_value=1.0
)

if st.button("Deposit"):

    response = requests.put(
        f"http://127.0.0.1:8000/customer/deposit/{customer_id}",
        json={"amount": amount}
    )

    st.success(
        response.json()["message"]
    )