import streamlit as st
import requests
import pandas as pd

st.title("📄 Mini Statement")

account_number = st.text_input(
    "Account Number"
)

transactions = requests.get(
    "http://127.0.0.1:8000/transactions/"
).json()

if account_number:

    filtered = []

    for tx in transactions:

        if tx["account_number"] == account_number:

            filtered.append(tx)

    if len(filtered) == 0:

        st.warning(
            "No Transactions Found"
        )

    else:

        df = pd.DataFrame(filtered)

        st.dataframe(
            df,
            use_container_width=True
        )