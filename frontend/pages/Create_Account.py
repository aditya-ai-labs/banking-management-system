import streamlit as st
import requests

st.title("➕ Create Account")

name = st.text_input("Customer Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

if st.button("Create Account"):

    data = {
        "name": name,
        "email": email,
        "phone": phone
    }

    response = requests.post(
        "http://127.0.0.1:8000/customer/create",
        json=data
    )

    result = response.json()

    st.success(
        f"Account Created Successfully\n\nAccount No: {result['account_number']}"
    )