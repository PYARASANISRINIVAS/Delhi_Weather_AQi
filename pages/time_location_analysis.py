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
                Time Based Analysis
            </h2>
            <ul>
                <li>
                    Which period of time does pollution increase the most during the day?
                </li>
                <li>
                    How does AQI vary across weekdays and weekends?
                </li>
            </ul>
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Location Based Analysis
            </h2>
            <ul>
                <li>
                    Which zones in Delhi experience the highest pollution levels?
                </li>
                <li>
                    How does pollution vary across residential, industrial, and commercial zones?
                </li>
                <li>
                    Which locations are most sensitive to weather changes?
                </li>
            </ul>
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. Which Period of Time Does Pollution Increase the Most During the Day?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)


    with st.echo():

        fig, ax = plt.subplots(figsize=(10,5))

        sns.lineplot(
            x=df['datetime'].dt.hour,
            y=df['aqi_index'],
            hue=df['location'],
            errorbar=None,
            ax=ax
        )

        plt.xticks(range(24))

        plt.xlabel("Hours")
        plt.ylabel("AQI Index")
        plt.title("Hourly AQI Trend Across Locations")

        st.pyplot(fig)

        plt.close(fig)


with st.container():

    with st.echo():

        g = sns.relplot(
            x=df['datetime'].dt.hour,
            y=df['aqi_index'],
            col=df['location'],
            col_wrap=3,
            errorbar=None,
            kind='line'
        )

        st.pyplot(g.fig)

        plt.close(g.fig)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li>
                AQI remains <span style="font-weight:bold;">consistently high throughout the day</span> across all locations.
            </li>
            <li>
                <span style="font-weight:bold;">IGI Airport</span> recorded the highest AQI levels overall (~254–260).
            </li>
            <li>
                <span style="font-weight:bold;">Rohini</span> showed comparatively lower AQI than other locations.
            </li>
            <li>
                Pollution levels gradually <span style="font-weight:bold;">increase during evening hours (5 PM – 8 PM)</span>.
            </li>
            <li>
                The peak AQI is observed around <span style="font-weight:bold;">6 PM to 7 PM</span>, likely due to traffic and human activity.
            </li>
            <li>
                After 8 PM, AQI starts slightly decreasing.
            </li>
            <li>
                Morning and late-night hours show relatively stable pollution levels.
            </li>
            <li>
                Most locations follow a similar hourly trend, indicating city-wide pollution influence.
            </li>
        </ul>

        <h3 class="h_container">Conclusion</h3>

        <ul>
            <li>
                <span style="font-weight:bold;">Evening hours experience the worst air quality.</span>
            </li>
            <li>
                <span style="font-weight:bold;">Traffic and urban activities strongly affect AQI during peak hours.</span>
            </li>
            <li>
                Delhi maintains consistently high pollution levels throughout the day.
            </li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. How Does AQI Vary Across Weekdays and Weekends?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Feature Creation - Day
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():

        day_order = [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]

        df['day'] = pd.Categorical(
            df['datetime'].dt.day_name(),
            categories=day_order,
            ordered=True
        )

    with st.echo():
        fig, ax = plt.subplots(figsize=(10,5))

        sns.lineplot(
            x=df['day'],
            y=df['aqi_index'],
            ax=ax
        )

        plt.xlabel("Days")
        plt.ylabel("AQI Index")
        plt.title("Weekly AQI Trend")

        st.pyplot(fig)

        plt.close(fig)


with st.container():
    with st.echo():

        g = sns.relplot(
            x=df['day'],
            y=df['aqi_index'],
            col=df['location'],
            kind='line',
            col_wrap=3
        )

        for ax in g.axes.flat:
            ax.tick_params(axis='x', rotation=45)

        st.pyplot(g.fig)

        plt.close(g.fig)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li>
                <span style="font-weight:bold;">Saturday</span> recorded the highest AQI levels during the week.
            </li>
            <li>
                <span style="font-weight:bold;">Tuesday</span> had the lowest AQI, indicating comparatively cleaner air.
            </li>
            <li>
                AQI gradually <span style="font-weight:bold;">increases from Thursday to Saturday</span>.
            </li>
            <li>
                <span style="font-weight:bold;">Weekend pollution levels</span> are slightly higher than weekdays.
            </li>
            <li>
                The AQI variation across the week is moderate and stable without extreme fluctuations.
            </li>
            <li>
                <span style="font-weight:bold;">Friday and Saturday</span> consistently show elevated pollution levels, possibly due to increased traffic and human activities.
            </li>
        </ul>

        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li>
                <span style="font-weight:bold;">Air quality worsens toward the weekend.</span>
            </li>
            <li>
                <span style="font-weight:bold;">Mid-week days experience comparatively better air quality.</span>
            </li>
            <li>
                Pollution remains consistently high throughout the week, showing persistent urban pollution impact.
            </li>
        </ul>
        </div>
        <br>
    """, unsafe_allow_html=True)




    # location based analysis 

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container"> Location Based Analysis </h3>
        """, unsafe_allow_html=True)
                

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. Which Zones in Delhi Experience the Highest Pollution Levels?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Feature Creation - Zone
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():

        def zones(loc):

            res = ['Dwarka','Rohini','Anand Vihar']
            ind = ['Okhla Phase III']
            com = ['Connaught Place','IGI Airport']

            if loc in res:
                return "Residential"

            elif loc in ind:
                return "Industry"

            else:
                return "Commercial"


        df['Zones'] = df['location'].apply(zones)

        
   

    with st.echo():
        fig, ax = plt.subplots(figsize=(8,5))
        sns.lineplot(
            x=df['Zones'],
            y=df['aqi_index'],
            ax=ax
        )

        plt.xlabel("Zones")
        plt.ylabel("AQI Index")
        plt.title("AQI Levels Across Different Zones")

        st.pyplot(fig)

        plt.close(fig)

with st.container():

    with st.echo():

        df.groupby('Zones')[
            ['pm2_5', 'pm10', 'co', 'no2']
        ].mean().reset_index()

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. How Does Pollution Vary Across Different Zones?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    st.error("Graphs are being created live... it may take a few seconds to render ⏳")

    with st.echo():

        z = df['Zones'].unique().tolist()

        for i in z:

            fig, ax = plt.subplots(figsize=(3,2))

            x = df.groupby('Zones')[
                ['pm2_5', 'pm10', 'co', 'no2']
            ].get_group(i).mean()

            a = sns.barplot(
                x=x.index,
                y=x.values,
            )

            # Bar label size
            for bars in a.containers:
                plt.bar_label(
                    bars,
                    fontsize=3,
                )

            # Axis label size
            plt.xlabel(i, fontsize=4)

            # Tick label sizes
            plt.xticks(fontsize=3)
            plt.yticks(fontsize=3)

            # Title size if needed
            # plt.title("...", fontsize=5)

            st.pyplot(fig)

            plt.close(fig)
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li>
                <span style="font-weight:bold;">Industrial areas</span> recorded the highest pollution levels among all area types.
            </li>
            <li>
                <span style="font-weight:bold;">CO (Carbon Monoxide)</span> is the dominant pollutant across residential, commercial, and industrial areas.
            </li>
            <li>
                <span style="font-weight:bold;">PM10 levels</span> are significantly higher in industrial areas, indicating strong dust and industrial emission impact.
            </li>
            <li>
                Commercial areas show slightly higher pollution levels than residential areas due to traffic and business activities.
            </li>
            <li>
                Residential areas recorded the lowest overall pollutant concentrations compared to commercial and industrial zones.
            </li>
            <li>
                <span style="font-weight:bold;">NO₂ levels</span> remain comparatively lower than other pollutants in all area categories.
            </li>
            <li>
                Pollution levels consistently increase from:
                <br>
                <span style="font-weight:bold;">
                    Residential → Commercial → Industrial
                </span>
            </li>
        </ul>

        <h3 class="h_container">Conclusion</h3>

        <ul>
            <li>
                Industrial activities and urban traffic are major contributors to pollution levels.
            </li>
            <li>
                Industrial zones experience the highest pollutant concentration, especially for CO and PM10.
            </li>
            <li>
                Residential areas are comparatively less polluted but still affected by urban emissions.
            </li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. Which Locations Are Most Sensitive to Weather Changes?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    st.error("Graphs are being created live... it may take a few seconds to render ⏳")

    with st.echo():

        fig, ax = plt.subplots(figsize=(15,5))

        sns.countplot(
            x=df['location'],
            hue=df['weather'],
            ax=ax
        )

        plt.xticks(rotation=45)

        plt.xlabel("Locations")
        plt.ylabel("Count")
        plt.title("Weather Distribution Across Locations")

        st.pyplot(fig)

        plt.close(fig)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li>
                <span style="font-weight:bold;">Clear sky weather</span> is the most frequently observed condition across all locations.
            </li>
            <li>
                <span style="font-weight:bold;">Overcast weather</span> is the second most common weather condition.
            </li>
            <li>
                Rainy conditions occur much less frequently compared to dry weather.
            </li>
            <li>
                <span style="font-weight:bold;">Fog occurrences</span> are very low but still important because they increase pollution trapping.
            </li>
            <li>
                All locations show almost similar weather distribution patterns, indicating consistent regional climate conditions.
            </li>
            <li>
                <span style="font-weight:bold;">Dwarka</span> and <span style="font-weight:bold;">IGI Airport</span> show slightly higher counts for cloudy and overcast conditions.
            </li>
            <li>
                Drizzle and dense drizzle events are comparatively rare throughout the dataset.
            </li>
        </ul>

        <h3 class="h_container">Conclusion</h3>

        <ul>
            <li>
                Delhi experiences mostly dry and clear weather conditions, which supports pollution accumulation.
            </li>
            <li>
                Rainfall events are limited, reducing natural pollutant cleansing opportunities.
            </li>
            <li>
                Similar weather patterns across locations indicate that pollution differences are mainly influenced by traffic, industrial activity, and local emissions.
            </li>
        </ul>
        </div>
        <br>
    """, unsafe_allow_html=True)