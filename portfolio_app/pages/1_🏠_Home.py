import streamlit as st
import os

current_dir = os.path.dirname(__file__) 
img_path = os.path.join(current_dir, "MYID2.png")

st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background: #F5F2FF;
        }

        [data-testid="stSidebar"] {
            background: #EBE6FF;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("✨ Future Developer ✨")

col1, col2 = st.columns([1,2])

with col1:
    # 2. RENDER CHECK
    if os.path.exists(img_path):
        st.image(img_path)
    else:
        # This will tell you if the file name is wrong or missing in 'pages'
        st.error(f"Image not found in pages folder: {img_path}")

with col2:
    st.info("Hi, I'm Rica Mae Sinogbujan👋!")
    st.info("I am a passionate student developer creating modern applications.")
    st.info("I build efficient, offline-capable systems and modern user interfaces.") 
