import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot  as plt 
import seaborn as sns

import time

st.markdown("""
            <h2 style="text-align:center; ">  Cleaning the data set   </h2>
            <hr> 

            """,unsafe_allow_html=True)

df=pd.read_csv("data/DelhiWeatherAqi_2025.csv")

with st.echo():
    st.write(df.dtypes)


# **Observations about the incorrect features**


with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" > Observations about the incorrect features </h3>
            <p class="p_container"> date_ist is of string type need  Date time format</p>
            <p class="p_container">  time_istis of string type need  date time format</p>
            <p class="p_container"> description is duplicate of the condition_text column</p>
        </div>
""", unsafe_allow_html=True)



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container" >  Handling the incorrect features</h3>
        <ul>
            <li>Adding a new feature <span style="font-weight:bold;">Datetime</span> by combining <span style="font-weight:bold;">date_ist</span> and <span style="font-weight:bold;">time_ist</span></li>
            <li>Dropping the <span style="font-weight:bold;">date_ist</span> and <span style="font-weight:bold;">time_ist</span> features</li>
            <li>Dropping the <span style="font-weight:bold;">description</span> feature</li>
            <li>Renaming the column names</li>
            <li>Rearranging the features</li>
        </ul>  
        </div>
        <br>

     """, unsafe_allow_html=True)    



with st.echo():
    
    
    df['datetime']=pd.to_datetime(df['date_ist']+" "+df['time_ist'],format='%d/%m/%Y %H:%M') # Adding new Feature Datetime By combining the date_ist and time_ist
    

    # dropping the unwanted features
    df.drop(columns=['date_ist','time_ist','description'],inplace=True)

    # renaming the column names
    df.rename(columns={"temp_c":"temp","pressure_mb":"pressure","windspeed_kph":"windspeed","condition_text":"weather"},inplace=True)

    # rearranging the features
    df=df[[ 'datetime',
    'location',
    'lat',
    'lon',
    'temp',
    'humidity',
    'pressure',
    'windspeed',
    'weather',
    'aqi_index',
    'pm2_5',
    'pm10',
    'co',
    'no2'
    ]]

    st.write(df.head(1))

# verification 

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Need Verification</h3>
        <ul>
            <li><span style="font-weight:bold;">Location</span> format checking</li>
            <li><span style="font-weight:bold;">Weather</span> format checking</li>
            <li>Checking whether any <span style="font-weight:bold;">date</span> values are missing</li>
            <li>Checking whether any <span style="font-weight:bold;">place name</span> exists for the given <span style="font-weight:bold;">latitude</span> and <span style="font-weight:bold;">longitude</span></li>
            <li>Checking whether <span style="font-weight:bold;">Humidity</span> values are within the range <span style="font-weight:bold;">(0-100)</span></li>
            <li>Checking whether <span style="font-weight:bold;">AQI Index</span> values are within the range <span style="font-weight:bold;">(0-500)</span></li>
            <li>Checking whether <span style="font-weight:bold;">pm2.5</span>, <span style="font-weight:bold;">pm10</span>, <span style="font-weight:bold;">co</span>, and <span style="font-weight:bold;">no2</span> contain any negative values</li>
            <li>Checking for any <span style="font-weight:bold;">Null values</span></li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.echo():
    st.write(df['location'].value_counts()) # checking  formating of column location

with st.echo():
    st.write(df['weather'].value_counts()) # checking  formating of column weather 



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li>The <span style="font-weight:bold;">locations</span> and <span style="font-weight:bold;">weather</span> features are correctly formatted with proper spelling and consistent letter casing, so no data handling is required.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.echo():
    st.write(df.groupby('location')['lat'].nunique()) # Any wrong  place name for given lat


with st.echo():
    st.write(df.groupby('location')['lon'].nunique()) # Any wrong  place name for given lat


with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li>Each <span style="font-weight:bold;">location</span> is mapped to only one unique <span style="font-weight:bold;">latitude</span> and <span style="font-weight:bold;">longitude</span> value.</li>
            <li>No incorrect or mismatched <span style="font-weight:bold;">place names</span> were found for the given coordinates.</li>
                </div>
           <br>
    """, unsafe_allow_html=True)


with st.container():
    with st.echo():
        st.write(f"<h4 style='color:white;'>Humidity range : {df['humidity'].min()} - {df['humidity'].max()}</h4>",unsafe_allow_html=True)
        st.write(f"<h4 style='color:white;'>AQI_index  range : {df['aqi_index'].min()}-{df['aqi_index'].max()}</h4>",unsafe_allow_html=True)



with st.echo():
    result = (df['aqi_index'] > 500).value_counts()
    result.index = result.index.astype(str)
    st.write(result)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Observation</h3>
        <ul>
            <li>There are <span style="font-weight:bold;">6903 AQI values</span> beyond the expected range limit, indicating  extreme pollution conditions that require further validation and preprocessing.</li>
            <li><span style="font-weight:bold;">Humidity </span>Values are with in the range</li>
       
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.echo():
    pass
    






st.markdown("### **Analyzing the reason for aqi index out of range**")

with st.echo():
    st.write(df[df['aqi_index']>500].groupby('location').count())


with st.echo():
    x=df[df['aqi_index']>500].groupby('location')
    st.write(x.get_group('Dwarka').groupby(df['datetime'].dt.month).head(5))
    
with st.echo():
    st.write(x.get_group('IGI Airport').groupby(df['datetime'].dt.month).head(5))
    
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Reason</h3>
        <ul>
            <li>According to <span style="font-weight:bold;">CPCB (Central Pollution Control Board)</span> and standard AQI guidelines, the AQI scale is officially bounded between <span style="font-weight:bold;">0 and 500</span>.</li>
            <li>Some pollutant concentrations exceeded the highest defined breakpoint ranges, causing the interpolation formula to mathematically generate AQI values above 500.</li>
            <li>Since AQI values beyond 500 are not categorized separately and are all considered <span style="font-weight:bold;">"Severe"</span>, the AQI values were clipped to 500 to maintain compliance with the standard AQI scale.</li>
        </ul>  
        </div>
        <br>

        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li>The <span style="font-weight:bold;">AQI values</span> exceeded 500 due to extremely high pollutant concentrations, so the values were clipped to <span style="font-weight:bold;">500</span> to follow the standard AQI guidelines.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)

st.markdown("### Checking PM2.5 / PM10 / CO / NO₂ Should Not Contain Any Negative Values")



with st.container():
    with st.echo():
        st.write(f"<h4 style='color:white;'>PM2.5 range : {df['pm2_5'].min()} - {df['pm2_5'].max()}</h4>", unsafe_allow_html=True)
        st.write(f"<h4 style='color:white;'>PM10 range : {df['pm10'].min()} - {df['pm10'].max()}</h4>", unsafe_allow_html=True)
        st.write(f"<h4 style='color:white;'>CO range : {df['co'].min()} - {df['co'].max()}</h4>", unsafe_allow_html=True)
        st.write(f"<h4 style='color:white;'>NO₂ range : {df['no2'].min()} - {df['no2'].max()}</h4>", unsafe_allow_html=True)


with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li>There are no negative values present in the <span style="font-weight:bold;">PM2.5</span>, <span style="font-weight:bold;">PM10</span>, <span style="font-weight:bold;">CO</span>, and <span style="font-weight:bold;">NO₂</span> pollutant features, so no additional data handling is required.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Overall Observations</h3>
        <ul>
            <li>The dataset contains properly formatted <span style="font-weight:bold;">location</span> and <span style="font-weight:bold;">weather</span> values with consistent spelling and letter casing.</li>
            <li>Some <span style="font-weight:bold;">AQI values</span> exceeded the standard AQI limit of 500 due to extremely high pollutant concentrations.</li>
            <li>A total of <span style="font-weight:bold;">6903 AQI values</span> were found beyond the valid AQI range and were clipped to 500 based on CPCB guidelines.</li>
            <li>The <span style="font-weight:bold;">humidity</span> values were verified to be within the valid range of 0–100.</li>
            <li>The pollutant features <span style="font-weight:bold;">PM2.5</span>, <span style="font-weight:bold;">PM10</span>, <span style="font-weight:bold;">CO</span>, and <span style="font-weight:bold;">NO₂</span> do not contain negative values.</li>
            <li>No invalid pollutant concentrations were identified, so no additional handling was required for these features.</li>
            <li>The dataset was validated successfully and cleaned to maintain consistency, accuracy, and compliance with AQI standards.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)


st.markdown("### Handling Out-of-Range AQI Values by Clipping Them to the Maximum Limit of 500")

with st.container():
    with st.echo():
        
        df.loc[df['aqi_index'] > 500, 'aqi_index'] = 500    # Handling AQI values greater than 500

with st.container():
    with st.echo():  
        st.write(df[df['aqi_index']>500].shape[0])

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">Identifying and Handling Null Values</h2>
        </div>
        <br>
    """, unsafe_allow_html=True)



with st.container():
    with st.echo():
        # Percentage of missing values
        st.write(df.isnull().sum())

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Observation</h3>
        <ul>
            <li>There are <span style="font-weight:bold;">no null values</span> present in the dataset.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)

# **Identifying any missing dates**

# x=df['datetime'].dt.month_name().value_counts()
# x
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">Identifying Any Missing Dates</h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():
        x = df['datetime'].dt.month_name().value_counts()
        st.write(x)
# df['location'].value_counts()


# plt.figure(figsize=(16,6))
# sns.countplot(x=df['datetime'].dt.month_name(),hue=df['location'])
# plt.title("Count of no of dates of each location")
# plt.xlabel('Months')
# plt.show()

st.markdown("**Visualizing the Monthly Date Distribution Across Locations**")

with st.container():
    with st.echo():
        plt.figure(figsize=(16,6))
        sns.countplot(
            x=df['datetime'].dt.month_name(),
            hue=df['location']
        )

        plt.title("Count of Number of Dates for Each Location")
        plt.xlabel("Months")
        plt.ylabel("Count")
        plt.xticks(rotation=45)

        plt.show()
        st.pyplot(plt)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Observation</h3>
        <ul>
            <li>The monthly date distribution shows that records are available for all months, indicating that there are <span style="font-weight:bold;">no completely missing months</span> in the dataset.</li>
            <li>Some months contain slightly different numbers of records because the number of days varies across months.</li>
            <li>The dataset appears to have a consistent time-series structure without major date gaps.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)





# **Identifying and Handling Duplicates**

# df.duplicated().sum()

# **conclusion** Their are no duplicated for the given data set .
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">Identifying and Handling Duplicates</h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():
        # Checking duplicate records
        duplicates = df.duplicated().sum()
        st.write(f"<h4 style='color:white;'>Duplicate records : {duplicates}</h4>",unsafe_allow_html=True)

    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Observation</h3>
        <ul>
            <li>There are <span style="font-weight:bold;">no duplicate records</span> present in the dataset, so no duplicate handling is required.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)

# **Identifying the outliers**



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">Identifying the Outliers</h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():
        parameters = [
            'temp', 'humidity', 'pressure',
            'windspeed', 'aqi_index',
            'pm2_5', 'pm10', 'co', 'no2'
        ]

        fig, ax = plt.subplots(3, 3, figsize=(15, 9))

        start = 0
        count = 0

        for col in parameters:

            sns.boxplot(
                x=df[col],
                ax=ax[start][count]
            )

            ax[start][count].set_title(f'Boxplot of {col}')

            if count == 2:
                start += 1
                count = 0
            else:
                count += 1
        plt.tight_layout()
        st.pyplot(fig)

# **Observation** : There are extreme large values in the data of every numerical column except in temparature and humidity column and they are very important to analyze where extreme values and when it is raising so i am not handling it .
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Observation</h3>
        <ul>
            <li>Extreme values are present in almost all numerical features except the <span style="font-weight:bold;">temperature</span>,<span style="font-weight:bold;">humidity</span> and <span style="font-weight:bold;">pressure</span> columns.</li>
            <li>These extreme values are important for analyzing unusual weather and pollution conditions, so they should not be removed directly.</li>
            <li>Since the outliers may represent real-world environmental conditions, no outlier handling was performed.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li>The dataset has been <span style="font-weight:bold;">successfully cleaned and validated</span> by handling range issues, verifying missing values, checking duplicates, and validating pollutant measurements.</li>
            <li>Further <span style="font-weight:bold;">feature engineering</span> and <span style="font-weight:bold;">feature creation</span> will be performed in the next stage of analysis based on the project requirements.</li>
        </ul>  
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" >Let's generate the insights use the side bar </h3>          

       </div>
""", unsafe_allow_html=True)
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" >-------------END---------</h3>          

       </div>
""", unsafe_allow_html=True)
    
# df.dtypes
# df.to_csv("data/DelhiWeatherAqi_2025_Cleaned_1.csv",index=False)
