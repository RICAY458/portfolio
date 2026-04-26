import streamlit as st

st.set_page_config(
    page_title="My Portfolio",
    page_icon="✨",
    layout="wide"
)

# Custom CSS for modern UI
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: #F5F2FF;
        }

        [data-testid="stSidebar"] {
            background: #EBE6FF;

        }

        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #1c1f26;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Welcome to My Professional Portfolio")
st.info("Navigate through the sidebar to know more about my work and skills.")
