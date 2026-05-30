import streamlit as st
import requests
import pandas as pd

st.title("💳 Transaction History")

response = requests.get(
    "http://127.0.0.1:8000/transactions/"
)

transactions = response.json()

if len(transactions) == 0:

    st.warning(
        "No Transactions Found"
    )

else:

    df = pd.DataFrame(
        transactions
    )

    st.subheader(
    "Recent Transactions"
)

    st.dataframe(
        df.tail(10),
        use_container_width=True
    )