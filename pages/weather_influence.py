import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

df = pd.read_csv(
    "data/DelhiWeatherAqi_2025_Cleaned_1.csv",
    parse_dates=['datetime']
)

st.markdown("""
            <h2 style="text-align:center; ">  Key Question Analysis   </h2>
            <hr> 
            """,unsafe_allow_html=True)



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Weather Influence Analysis
            </h2>
            <ul>
                <li>Behaviour of temperature in different locations throughout the year</li>
                <li>How do weather conditions (temperature, humidity, wind speed, pressure) influence AQI levels?</li>
                <li>Does higher wind speed help in reducing or increasing pollution levels?</li>
                <li>Are there weather patterns in pollution levels?</li>
            </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)



    #   Q. Behaviour of Temperature in Different Locations Throughout the Year
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. Behaviour of Temperature in Different Locations Throughout the Year
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)


    with st.echo():

        fig, ax = plt.subplots(figsize=(18,6))

        sns.lineplot(
            y=df['temp'],
            x=df['datetime'].dt.month_name(),
            hue=df['location'],
            errorbar=None,
            ax=ax
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

        plt.close(fig)


with st.container():

    with st.echo():

        fig, ax = plt.subplots(figsize=(10,5))

        a = sns.barplot(
            x=df['location'],
            y=df['temp'],
            errorbar=None,
            ax=ax
        )

        plt.title("Average Temperature Location Wise")

        for bar in a.containers:
            plt.bar_label(bar)

        st.pyplot(fig)

        plt.close(fig)
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li>Temperature gradually <span style="font-weight:bold;">increases from January to June</span> across all locations.</li>
            <li><span style="font-weight:bold;">May and June</span> recorded the highest temperatures (~32°C).</li>
            <li>After June, temperature starts <span style="font-weight:bold;">decreasing slowly</span> toward winter.</li>
            <li><span style="font-weight:bold;">December and January</span> had the lowest temperatures (~14–16°C).</li>
            <li>All locations show very similar temperature patterns, indicating uniform seasonal climate across Delhi.</li>
            <li><span style="font-weight:bold;">September</span> shows a slight rise again before temperatures drop sharply from October onward.</li>
            <li>Seasonal transition is clearly visible:
                <ul>
                    <li><span style="font-weight:bold;">Summer:</span> April–June</li>
                    <li><span style="font-weight:bold;">Monsoon:</span> July–September</li>
                    <li><span style="font-weight:bold;">Winter:</span> November–January</li>
                </ul>
            </li>
        </ul>

        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li>Delhi experiences <span style="font-weight:bold;">extreme seasonal variation</span> with very hot summers and cool winters.</li>
            <li>Temperature patterns remain <span style="font-weight:bold;">consistent across all monitored locations</span>.</li>
            <li>Peak summer months may contribute to increased dust and particulate pollution levels.</li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)

# Q. How Do Weather Conditions (Temperature, Humidity, Wind Speed, Pressure) Influence AQI Levels?

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. How Do Weather Conditions (Temperature, Humidity, Wind Speed, Pressure) Influence AQI Levels?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)


    with st.echo():

        cor = df[['aqi_index','temp','humidity','pressure','windspeed']].corr()
        fig, ax = plt.subplots(figsize=(7,5))
        sns.heatmap(cor, annot=True, ax=ax)
        st.pyplot(fig)
        plt.close(fig)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li><span style="font-weight:bold;">AQI and humidity</span> have a moderate negative correlation (-0.42), meaning higher humidity generally helps reduce pollution levels.</li>
            <li><span style="font-weight:bold;">AQI and temperature</span> show a weak positive correlation (0.23), indicating pollution slightly increases during hotter conditions.</li>
            <li><span style="font-weight:bold;">AQI and wind speed</span> have a small positive relation (0.16), showing wind has limited direct impact on AQI.</li>
            <li><span style="font-weight:bold;">Temperature and pressure</span> have a strong negative correlation (-0.72).</li>
            <li><span style="font-weight:bold;">Temperature and humidity</span> also show a moderate negative relationship (-0.51).</li>
            <li><span style="font-weight:bold;">Pressure</span> has very weak relation with AQI (-0.13).</li>
        </ul>

        <h3 class="h_container">Conclusion</h3>

        <ul>
            <li><span style="font-weight:bold;">Humidity</span> plays an important role in reducing AQI levels.</li>
            <li><span style="font-weight:bold;">Hot and dry conditions</span> slightly increase pollution concentration.</li>
            <li>Weather conditions influence air quality, but particulate pollutants remain the major contributors to AQI changes.</li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)


# Q. Does Higher Wind Speed Help in Reducing or Increasing Pollution Levels?

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. Does Higher Wind Speed Help in Reducing or Increasing Pollution Levels?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)


    with st.echo():

        fig, ax = plt.subplots(figsize=(15,5))

        sns.lineplot(
            x=df['datetime'].dt.month_name(),
            y=df['windspeed'],
            ax=ax
        )

        sns.lineplot(
            x=df['datetime'].dt.month_name(),
            y=df['pm2_5'],
            ax=ax
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

        plt.close(fig)
    

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container">
                The above two columns are not comparable 
            </h3>
            <ul>
                <li>
                    The pollutant and weather features contain values in 
                    <span style="font-weight:bold;">different numerical ranges</span>, 
                    making direct comparison difficult.
                </li>
                <li>
                    Therefore, <span style="font-weight:bold;">Min-Max Scaling</span> 
                    was applied to re-scale all features into a common range of 
                    <span style="font-weight:bold;">0–1</span>.
                </li>
                <li>
                    This helps in better comparison, visualization, and understanding 
                    of the feature trends across different pollutants and weather conditions.
                </li>
            </ul>
        </div>
        <br>
    """, unsafe_allow_html=True)



with st.container():

    with st.echo():

        from sklearn.preprocessing import MinMaxScaler

        cols = ['windspeed', 'pm2_5', 'pm10', 'co', 'no2']

        scaler = MinMaxScaler()

        scaled_df = pd.DataFrame(
            scaler.fit_transform(df[cols]),
            columns=cols
        )

        fig, ax = plt.subplots(figsize=(15,5))

        sns.lineplot(
            x=df['datetime'].dt.month_name(),
            y=scaled_df['windspeed'],
            label="windspeed",
            ax=ax
        )

        sns.lineplot(
            x=df['datetime'].dt.month_name(),
            y=scaled_df['pm2_5'],
            label="pm2_5",
            ax=ax
        )

        sns.lineplot(
            x=df['datetime'].dt.month_name(),
            y=scaled_df['pm10'],
            label="pm10",
            ax=ax
        )

        sns.lineplot(
            x=df['datetime'].dt.month_name(),
            y=scaled_df['co'],
            label="co",
            ax=ax
        )

        sns.lineplot(
            x=df['datetime'].dt.month_name(),
            y=scaled_df['no2'],
            label="no2",
            ax=ax
        )

        plt.xticks(rotation=45)

        st.pyplot(fig)

        plt.close(fig)

with st.container():

    with st.echo():

        cor = df[['windspeed', 'pm2_5', 'pm10', 'co', 'no2']].corr()

        fig, ax = plt.subplots(figsize=(7,5))

        sns.heatmap(cor, annot=True, ax=ax)

        st.pyplot(fig)

        plt.close(fig)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li><span style="font-weight:bold;">Wind speed</span> has a negative correlation with <span style="font-weight:bold;">CO</span> and <span style="font-weight:bold;">NO₂</span>.</li>
            <li>Higher wind helps disperse harmful gases and improves air quality.</li>
            <li><span style="font-weight:bold;">PM2.5 and PM10</span> show a strong positive correlation (0.62).</li>
            <li><span style="font-weight:bold;">CO and NO₂</span> have a very strong positive correlation (0.73).</li>
            <li>Vehicular pollution contributes significantly to gaseous pollutants and fine particles.</li>
        </ul>

        <h3 class="h_container">Conclusion</h3>

        <ul>
            <li><span style="font-weight:bold;">Higher wind speeds</span> help reduce gaseous pollutants significantly.</li>
            <li><span style="font-weight:bold;">Traffic and fuel combustion</span> are major sources of CO and NO₂.</li>
            <li>Particulate matter pollution remains a major air quality concern.</li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)


with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. Are There Specific Weather Patterns That Influence Pollution Levels?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)


weather_order = [
    'Fog',
    'Clear sky',
    'Mainly clear',
    'Partly cloudy',
    'Overcast',
    'Drizzle: Light',
    'Drizzle: Moderate',
    'Drizzle: Dense',
    'Rain: Slight',
    'Rain: Moderate',
    'Rain: Heavy',
]

df['weather'] = pd.Categorical(
    df['weather'],
    categories=weather_order,
    ordered=True
)

df['weather'].value_counts()

with st.container():



    with st.echo():

        fig, ax = plt.subplots(figsize=(15,5))

        sns.lineplot(
            y=df['aqi_index'],
            x=df['weather'],
            ax=ax
        )

        plt.xticks(rotation=45)

        plt.xlabel("Weather Conditions")
        plt.ylabel("AQI Index")
        plt.title("Weather Conditions vs AQI Levels")

        st.pyplot(fig)

        plt.close(fig)

with st.container():

    with st.echo():

        fig, ax = plt.subplots(figsize=(15,5))

        sns.barplot(
            y=df['aqi_index'],
            x=df['weather'],
            order=weather_order,
            ax=ax
        )

        plt.xticks(rotation=45)

        plt.xlabel("Weather Conditions")
        plt.ylabel("Average AQI")
        plt.title("Average AQI Across Different Weather Conditions")

        st.pyplot(fig)

        plt.close(fig)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li><span style="font-weight:bold;">Clear sky conditions</span> recorded the highest AQI levels (~240). :contentReference[oaicite:0]{index=0}</li>
            <li><span style="font-weight:bold;">Partly cloudy</span> and <span style="font-weight:bold;">mainly clear</span> weather also showed high pollution levels. :contentReference[oaicite:1]{index=1}</li>
            <li><span style="font-weight:bold;">Rainy and drizzling conditions</span> had the lowest AQI values. :contentReference[oaicite:2]{index=2}</li>
            <li><span style="font-weight:bold;">Heavy rain</span> significantly reduced air pollution due to pollutant washout. :contentReference[oaicite:3]{index=3}</li>
            <li><span style="font-weight:bold;">Fog conditions</span> still showed high AQI because pollutants get trapped near the surface. :contentReference[oaicite:4]{index=4}</li>
            <li><span style="font-weight:bold;">Overcast weather</span> had slightly lower AQI compared to clear sky conditions. :contentReference[oaicite:5]{index=5}</li>
            <li>AQI generally decreases when <span style="font-weight:bold;">moisture and rainfall increase</span>. :contentReference[oaicite:6]{index=6}</li>
        </ul>

        <h3 class="h_container">Conclusion</h3>

        <ul>
            <li><span style="font-weight:bold;">Rainfall</span> helps improve air quality by removing pollutants from the atmosphere. :contentReference[oaicite:7]{index=7}</li>
            <li><span style="font-weight:bold;">Clear and dry weather conditions</span> increase pollution accumulation. :contentReference[oaicite:8]{index=8}</li>
            <li><span style="font-weight:bold;">Foggy weather</span> can worsen pollution by trapping pollutants close to the ground. :contentReference[oaicite:9]{index=9}</li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h3 class="h_container" style="text-align:center;">-------------END---------</h3>          

       </div>
""", unsafe_allow_html=True)