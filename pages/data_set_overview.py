import streamlit as st
import numpy as np
import pandas as pd

st.markdown("""
            <h2 style="text-align:center; ">  Understanding  the data set   </h2>
            <hr> 

            """,unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" >Dataset Description </h3>
            <p class="p_container"> The dataset used in this project contains comprehensive hourly Air Quality Index (AQI) and weather-related data collected from multiple monitoring locations across Delhi, India, during the year 2025. The dataset was designed to support detailed environmental analysis, pollution monitoring, and weather influence studies.</p>
                </div>
                <br> 
    """, unsafe_allow_html=True)    


#  loading the data set 
with st.echo():  

    df=pd.read_csv("data/DelhiWeatherAqi_2025.csv")      # reading the csv  
    st.write(df.head(5))        # first 5 elements 
     


with st.echo():
        st.write(df.shape)     # shape of the table (rows x columns)
   



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
                <h3 class="h_container" > Dataset Size</h3>
                <p class="p_container"> Total Records : Approximately 52,560 rows</p>
                <p class="p_container">Total Features : 16 columns </p>
                <p class="p_container"> Data Granularity : Hourly observations</p>
                <p class="p_container">Time Coverage : January 2025 – December 2025 </p>
                <p class="p_container"> The dataset combines both air pollution parameters and meteorological attributes to understand how environmental conditions influence air quality levels across different regions of Delhi.<p>
                </div>
     """, unsafe_allow_html=True)               


with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container" > Pollutants Included </h3>
        <ul>
                <li>PM2.5 </li>
                <li>PM10 </li>
                <li>NO₂ (Nitrogen Dioxide) </li>
                <li>CO (Carbon Monoxide) </li>
        </ul>
               
    

     """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container" >  Weather Parameters Included </h3>
        <ul>
                <li>Temperature</li>
                <li>Humidity</li>
                <li>Wind Speed</li>
                <li>Atmospheric Pressure</li>
                <li>Weather conditions</li>
        </ul>
               
    

     """, unsafe_allow_html=True)          

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container" > Locations Covered </h3>
        <p class="p_container"> The dataset includes monitoring stations from different zones of Delhi representing residential, commercial, and industrial regions.</p>
    
        <ul>
            <li>
                Residential Zones
                <ul>
                    <li>Dwarka</li>
                    <li>Rohini</li>
                    <li>Anand Vihar</li>
                 </ul>
            </li>
            <li>
                Commercial Zones
                <ul>
                    <li>Connaught Place</li>
                    <li>IGI Airport</li>
                </ul>
            </li>
            <li>
                Industrial Zones
                <ul>
                    <li>Okhla Phase III</li>
                </ul>
            </li>
        </ul>
                </div> 
               
    

     """, unsafe_allow_html=True)          







st.subheader("Categorization  of the Features and Their description")


# ----------------------------------------------------------------------



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container" >Real Numerical Columns  </h3>                
            <ul style="font-size:18px;"> 
                <li> <span style = "font-weight: bold; "> temp_c</span> : Ambient Temperature Celsius (°C) hot - cold - moderate  </li>
                <li> <span style = "font-weight: bold; "> humidity</span> : Relative Humidity Percentage (%)</li>
                <li> <span style = "font-weight: bold; "> pressure_mb</span> : Atmospheric Pressure Millibars (mb) </li>
                <li> <span style = "font-weight: bold; "> windspeed_kph</span> : Wind Speed Kilometers per hour (kph)</li>
                <li> <span style = "font-weight: bold; "> aqi_index </span> : Air Quality Index Value (Numerical Index)</li>
                <li> <span style = "font-weight: bold; "> pm2_5</span> : Particulate Matter < 2.5 micrometers ( µg/m³)</li>
                <li> <span style = "font-weight: bold; "> pm10</span> : Particulate Matter < 10 micrometers ( µg/m³ )</li>
                <li> <span style = "font-weight: bold; "> co </span> : Carbon Monoxide concentration ( µg/m³ )</li>
                <li> <span style = "font-weight: bold; ">no2 </span> : Nitrogen Dioxide concentration ( µg/m³ ) ( µg/m³ )</li>
            </ul>
 
       </div> 
""", unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" >categorical / discrete numerical columns </h3>          
            <ul style="font-size:18px;"> 
                <li> <span style = "font-weight: bold; "> location </span> : Specific location within Delhi </li>
                <li> <span style = "font-weight: bold; "> date_ist/span> : Date of the observation (Indian Standard Time)(DD/MM/YYYY)</li>
                <li> <span style = "font-weight: bold; "> condition_text</span> : Weather Condition Description Text. </li>
                <li> <span style = "font-weight: bold; "> time_ist</span> :Time of the observation (Indian Standard Time)(H:MM (24-hour format))</li>
                <li> <span style = "font-weight: bold; "> lat</span> : Latitude of the location</li>
                <li> <span style = "font-weight: bold; "> lon</span> : Longitude of the location</li>
                <li> <span style = "font-weight: bold; "> description</span> : WMO Weather Code Description </li>
            </ul>
       </div>
""", unsafe_allow_html=True)
    
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" >Let's do the cleaning use side bar for navigation.....</h3>          

       </div>
""", unsafe_allow_html=True)
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px; text-align:center;">
            <h3 class="h_container" style="text-align:center;">-------------END---------</h3>          

       </div>
""", unsafe_allow_html=True)
    



