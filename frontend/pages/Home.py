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

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class="card">
    <h2>👥</h2>
    <h3>Customers</h3>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h2>💰</h2>
    <h3>Deposits</h3>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h2>💸</h2>
    <h3>Withdrawals</h3>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class="card">
    <h2>📊</h2>
    <h3>Reports</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.info(
    "Use the sidebar to access banking modules."
)