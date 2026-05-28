import streamlit as st
import time



st.markdown("""<h2 style="margin : 0px; padding : 0px ; text-align :center" > Decoding Delhi’s Air Quality  <br>  <span style=" font-weight:normal; font-size :33px" >  Exploring Air Pollution Patterns and Weather Influence in 2025 </span> </h2>""",unsafe_allow_html=True)
st.markdown("<hr>",unsafe_allow_html=True)
time.sleep(1)


# Intoduction 

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" >Introduction</h3>
                <p class="p_container"> Air pollution is one of the major environmental challenges affecting human health and urban development. Rapid urbanization, industrial growth, vehicular emissions, and changing weather conditions contribute significantly to the deterioration of air quality.</p>
                <p class="p_container"> Air pollution in Delhi has become a critical environmental and public health issue. Despite continuous monitoring, pollution levels fluctuate significantly across different locations and time periods, making it difficult to implement timely and effective pollution control measures.</p> 
        </div>
""", unsafe_allow_html=True)

# Problem Statement


with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" >Problem Statement</h3>
            <p class="p_container"> Modern urban management requires a deeper understanding of how environmental and meteorological factors influence air quality. Monitoring and analyzing environmental data is essential for identifying pollution patterns and understanding the factors affecting AQI levels.</p>
            <p class="p_container">This project focuses on analyzing hourly AQI and weather data across multiple locations in Delhi to uncover patterns, trends, and relationships that influence pollution levels.</p>
        </div>
""", unsafe_allow_html=True)
    


# VIDEO full video 


with st.container():

    st.markdown("""
         <div class="custom-box"> <h3 class="h_container">Complete Project Explanation Video </h3> 
                <p class="p_container">🎥 In this video, I have explained my complete data analysis project on Delhi’s Air Quality. </p>
        </div>
                
        </div> <br> """, unsafe_allow_html=True)

    url="assets/explanation.mp4"
    st.video(
        url,
        autoplay=False
    )
    

# objective of this analysis 


with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container" >Objective of the Analysis</h3>
                <ul class="p_container">
                    <li > To perform Exploratory Data Analysis (EDA) on Delhi’s AQI and weather dataset.</li>
                    <li>To identify trends and patterns in air pollution levels across different locations.</li>
                    <li> To study the impact of pollutants such as PM2.5, PM10, NO₂, and CO on air quality.</li>
                    <li>To identify high-risk pollution periods and pollution-prone locations.</li>
                    <li> To generate meaningful insights using statistical analysis and data visualization techniques.</li>
                </ul>
""", unsafe_allow_html=True)
    
# Tools used 

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container" >Tools Used</h3>
                <ul class="p_container">
                    <li > Python </li>
                    <li > Numpy </li>
                    <li >Pandas </li>
                    <li > Matplotlib</li>
                    <li > Seaborn </li>
                </ul>
""", unsafe_allow_html=True)



