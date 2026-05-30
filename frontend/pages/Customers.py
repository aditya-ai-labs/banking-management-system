import streamlit as st
import requests
import pandas as pd

st.title("👥 Customers")

search = st.text_input(
    "🔍 Search Customer"
)

response = requests.get(
    "http://127.0.0.1:8000/customer/all"
)

customers = response.json()

if search:

    customers = [
        c
        for c in customers
        if search.lower()
        in c["name"].lower()
    ]

if customers:

    for customer in customers:

        with st.container():

            st.markdown(f"""
            ### {customer['name']}

            Account No:
            {customer['account_number']}

            Balance:
            ₹ {customer['balance']}
            """)

            st.divider()

else:

    st.warning(
        "No Customer Found"
    )