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
        
        .card {
            padding: 20px;
            border-radius: 15px;
            background-color: #ffffff;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            height: 150px; /* Added fixed height for alignment */
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("✨ My Portfolio ✨")
st.subheader("Future Developer")

col1, col2 = st.columns([1,2])

with col1:
    # 2. RENDER CHECK
    if os.path.exists(img_path):
        st.image(img_path)
    else:
        # This will tell you if the file name is wrong or missing in 'pages'
        st.error(f"Image not found in pages folder: {img_path}")

st.divider()

with col2:
    st.markdown("""
    ### Hi, I'm Rica Mae Sinogbujan👋!
    I am a passionate student developer creating modern applications.

    I build efficient, offline-capable systems and modern user interfaces.

    🚀 Explore my portfolio using the sidebar!
    """)
st.divider()
