import streamlit as st


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
            background-color: #B7C9E2;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("👤 About Me")

st.markdown("""
    <div class="card">
        I am a dedicated Computer Science student at DEBESMSCAT with hands-on experience in building applications and a passion for software development. 
        Despite being a student, I am willing to learn new technologies, and a commitment to continuous learning to support the company’s goals.
    </div>
""", unsafe_allow_html=True)

st.subheader("🎓 Education")

# --- START OF 3-COLUMN LAYOUT ---
# We create 3 columns to hold my 3 education levels
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Primary")
    st.info("Calumpang Elementary School")
    st.info("Calumpang, Cawayan, Masbate")
    st.info("2006-2013")

with col2:
    st.write("Secondary")
    st.info("Dalipe National High School")
    st.info("Dalipe, Cawayan, Masbate")
    st.info("2013-2019")

with col3:
    st.write("Tertiary")
    st.info("DEBESMSCAT - " 
    "Bachelor of Science in Computer Science")
    st.info("Cabitan, Mandaon, Masbate")
    st.info("2023 - Present")
# --- END OF 3-COLUMN LAYOUT ---


st.subheader("🚀 Goals")
st.info("- Anroid Developer ")
st.info("- Web Front-end Developer ")
st.info("For now I will continue to enhance my skills as a beginner to become a professional Developer.")
# Fun interaction
mood = st.selectbox("How do you feel about coding?", ["😃 Love it", "🙂 Like it", "😅 It's okay"])
st.write("Your answer:", mood)
