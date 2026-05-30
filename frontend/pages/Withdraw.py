import streamlit as st
import requests

st.title("💸 Withdraw Money")

customer_id = st.number_input(
    "Customer ID",
    min_value=1
)

amount = st.number_input(
    "Withdraw Amount",
    min_value=1.0
)

if st.button("Withdraw"):

    response = requests.put(
        f"http://127.0.0.1:8000/customer/withdraw/{customer_id}",
        json={"amount": amount}
    )

    st.success(
        response.json()["message"]
    )