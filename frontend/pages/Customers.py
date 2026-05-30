import streamlit as st
import requests

st.title("👥 Customer Directory")

search = st.text_input(
    "🔍 Search Account Number"
)

customers = requests.get(
    "http://127.0.0.1:8000/customer/all"
).json()

filtered = []

for customer in customers:

    if search == "":
        filtered.append(customer)

    elif search in customer["account_number"]:
        filtered.append(customer)

if len(filtered) == 0:

    st.warning(
        "No Customer Found"
    )

for customer in filtered:

    with st.expander(
        f"{customer['name']} | {customer['account_number']}"
    ):

        st.write(
            f"📧 {customer['email']}"
        )

        st.write(
            f"📱 {customer['phone']}"
        )

        st.write(
            f"💰 Balance: ₹ {customer['balance']}"
        )

        if customer["balance"] < 1000:

            st.error(
                "⚠ Low Balance Alert"
            )