import streamlit as st

st.set_page_config(
    page_title="Banking Management System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

[data-testid="stSidebar"]{
    background:#0f172a;
}

.main{
    background:#f8fafc;
}

</style>
""", unsafe_allow_html=True)

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2830/2830284.png",
    width=90
)

st.sidebar.title(
    "🏦 Banking System"
)

st.sidebar.markdown("---")

st.markdown("""
<div style="
background:linear-gradient(135deg,#1e3a8a,#2563eb);
padding:40px;
border-radius:20px;
color:white;
">

<h1>🏦 Banking Management System</h1>

<p>
Secure • Reliable • Modern Banking Dashboard
</p>

</div>
""", unsafe_allow_html=True)