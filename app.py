import streamlit as st


st.session_state.sidebar_opened = 0

# page congigurations 
st.set_page_config(
    page_title="Delhi AQI Analysis",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state='expanded'
)

# setting the background image and removing the header background color 
st.markdown(
    """
    <style>
    [data-testid="stIconMaterial"]{
    color:red
    }

    [data-testid="stHeader"] {
    background: None;
    }
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1506744038136-46273834b3fb");

        background-size: cover;
        # background-position: center;
        # background-attachment: fixed;
        # background-repeat: no-repeat;
    }

    .stMainBlockContainer , hr {
            margin-top: 0px;
            padding-top: 0px;
    }
    .custom-box {
    background: linear-gradient(135deg,#ffffff,#e0f2fe);
    padding: 30px;
    border-radius: 18px;
    border-left: 8px solid #0284c7;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.15);
    margin-top: 20px;
    font-family: "Times New Roman", serif;
    }
            
    .p_container{
    font-size: 18px ! important ;
    font-weight: 500;
    color: #0f172a;
    margin-bottom: 15px;
            
            }
    .h_container{
    font-size: 20px;
    line-height: 1.8;
    color: #334155;
    text-align: justify;
    }

    ul,li {
        font-size:18px
        }

    </style>

    
    """,
    unsafe_allow_html=True
)



pg = st.navigation([

    st.Page("pages/home.py",title="🏠 Home"),
    st.Page("pages/about_project.py",title="📘 About the Project"),
    st.Page("pages/data_set_overview.py",title="📊 Dataset Overview"),
    st.Page("pages/data_cleaning.py",title="🧹 Data Cleaning & Validation"),
    st.Page("pages/trend_analysis.py",title="📈 Pollution Trend & Impact Analysis"),
    st.Page("pages/weather_influence.py",title="🌦️ Weather Influence Analysis"),
    st.Page("pages/time_location_analysis.py",title="🕒 Time & Location Analysis"),
    st.Page("pages/overall_conclusion.py",title="📌 Overall Conclusion"),
    st.Page("pages/alerts_for_people.py",title="⚠️ Public Alerts & Safety Tips"),
    st.Page("pages/recommendations_govt.py",title="🏛️ Government Recommendations"),
    st.Page("pages/about_me.py",title="👨‍💻 About Me")
]).run()
