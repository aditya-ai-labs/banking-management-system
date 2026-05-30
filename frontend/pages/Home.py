import streamlit as st

st.markdown("""
<style>

.hero{

background:
linear-gradient(
135deg,
#0f172a,
#1e3a8a
);

padding:60px;

border-radius:20px;

color:white;

margin-bottom:30px;
}

.card{

background:white;

padding:25px;

border-radius:20px;

text-align:center;

box-shadow:
0px 5px 20px rgba(0,0,0,.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""

<div class="hero">

<h1>🏦 Smart Banking Dashboard</h1>

<p>
Manage customer accounts, deposits,
withdrawals and banking operations.
</p>

</div>

""", unsafe_allow_html=True)

import requests

customers = requests.get(
    "http://127.0.0.1:8000/customer/all"
).json()

transactions = requests.get(
    "http://127.0.0.1:8000/transactions/"
).json()

total_customers = len(customers)

total_transactions = len(transactions)

total_balance = sum(
    c["balance"]
    for c in customers
)

c1,c2,c3 = st.columns(3)

c1.metric(
    "Customers",
    total_customers
)

c2.metric(
    "Transactions",
    total_transactions
)

c3.metric(
    "Bank Balance",
    f"₹ {total_balance:,.0f}"
)

st.markdown("---")

st.info(
    "Use the sidebar to access banking modules."
)


st.markdown("---")

st.subheader(
    "🏦 Banking Services"
)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.success(
        "👤 Account Management"
    )

with c2:
    st.success(
        "💰 Deposits"
    )

with c3:
    st.success(
        "💸 Withdrawals"
    )

with c4:
    st.success(
        "📄 Mini Statement"
    )