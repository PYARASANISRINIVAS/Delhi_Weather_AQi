
import streamlit as st
import streamlit as st


st.markdown("""
            <h2 style="text-align:center; ">  ABOUT ME   </h2>
            <hr> 

            """,unsafe_allow_html=True)

st.title("👨‍💻 PYARASANI . SRINIVAS ")

with st.container():

    st.markdown("""
    <div class="custom-box" style="border-radius: 5px; padding:20px;">
            <p style="font-size:18px; line-height:1.8;">
             Hello! I am  <span style="font-weight:bold;">Pyarasani.Srinivas</span>  an aspiring 
            <span style="font-weight:bold;">Data Scientist</span> 
             and 
            <span style="font-weight:bold;">AI Enthusiast</span> 
         passionate about building real-world 
            <span style="font-weight:bold;">data analytics</span>, 
            <span style="font-weight:bold;">machine learning</span>, 
            and 
         <span style="font-weight:bold;">interactive dashboard projects</span>.
        I enjoy transforming raw data into meaningful insights through 
        visualization, feature engineering, and exploratory data analysis using 
        Python, Pandas, Matplotlib, Seaborn, and Streamlit.
        </p>
    </div>

    <br>
    """, unsafe_allow_html=True)

    st.link_button(
        "📓 Project Google Colab Notebook",
        "https://colab.research.google.com/drive/1jHsmMugMednoJUJ8HdWr_mmAkEiHhKwN?usp=sharing"
    )

with st.container():

    st.markdown("""
    <div class="custom-box" style="border-radius: 5px; padding:20px;">
        <h2 class="h_container">
            Connect With Me
        </h2>

    </div>
    <br>
    """, unsafe_allow_html=True)

c1,c2,c3=st.columns([1,1,1])
with c1:
    st.link_button(
        "🔗 LinkedIn Profile",
        "https://www.linkedin.com/in/pya-srinivas/",width="stretch"
    )
with c2:
    st.link_button(
        "💻 GitHub Profile",
        "https://github.com/PYARASANISRINIVAS?tab=repositories",width="stretch"
    )

with c3:
    st.link_button(
        " 📧 Email:pyarasanisrinivas16@gmail.com",
        "mailto:pyarasanisrinivas16@gmail.com",width="stretch"
    )



