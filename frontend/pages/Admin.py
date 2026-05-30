import streamlit as st
import requests
import pandas as pd

st.title("📊 Admin Dashboard")

response = requests.get(
    "http://127.0.0.1:8000/customer/all"
)

customers = response.json()

total_customers = len(customers)

total_balance = sum(
    c["balance"]
    for c in customers
)

avg_balance = (
    total_balance / total_customers
    if total_customers > 0
    else 0
)

c1,c2,c3 = st.columns(3)

c1.metric(
    "Customers",
    total_customers
)

c2.metric(
    "Bank Balance",
    f"₹ {total_balance:,.0f}"
)

c3.metric(
    "Average Balance",
    f"₹ {avg_balance:,.0f}"
)

st.markdown("---")

st.subheader(
    "Customer Management"
)

for customer in customers:

    col1,col2 = st.columns([8,1])

    with col1:

        st.write(
            f"👤 {customer['name']} | ₹ {customer['balance']}"
        )

    with col2:

        if st.button(
            "🗑",
            key=customer["id"]
        ):

            requests.delete(
                f"http://127.0.0.1:8000/customer/delete/{customer['id']}"
            )

            st.rerun()

st.markdown("---")

df = pd.DataFrame(customers)

st.dataframe(
    df,
    use_container_width=True
)