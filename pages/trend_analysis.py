import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import time

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
            <h2 class="h_container">Dataset After Cleaning</h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():
        st.write(df.head())

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                AQI Trend and Pollutant Analysis
            </h2>
            <ul>
                <li>What are the overall air pollution (AQI) trends across 2025?</li>
                <li>Which pollutants (PM2.5, PM10, NO₂, CO) contribute most to poor air quality?</li>
                <li>What is the relationship between PM10 and AQI across locations?</li>
                <li>How frequently does AQI reach unhealthy or hazardous levels?</li>
                <li>What is the percentage contribution of each AQI category?</li>
            </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)
with st.container():
    st.markdown("""
        <div style="
            background-color:#ff4b4b;
            padding:15px;
            border-radius:8px;
            color:white;
            font-weight:bold;
            font-size:18px;
        ">
            ⚠️ Graphs are being created live... it may take a few seconds to render.
        </div>
        <br>
    """, unsafe_allow_html=True)

#  Q.How was the overall air pollution (AQI) trends across 2025?
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">            
            <h2>Q.How was the overall air pollution (AQI) trends across 2025?</h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():
        time.sleep(2)
        plt.figure(figsize=(18,8))

        ax = sns.lineplot(
            y=df['aqi_index'],
            x=df['datetime'].dt.month_name(),
            hue=df['location'],
            marker='o'
        )

        plt.xticks(rotation=45)
        plt.xlabel("Months")
        plt.ylabel("AQI Index")
        plt.title("Monthly AQI Trends Across Locations")
        st.pyplot(plt)

    with st.echo():
        sns.relplot(
            data=df,
            x=df['datetime'].dt.month,
            y='aqi_index',
            kind='line',
            col='location',
            col_wrap=3
        )

        plt.tight_layout()
        st.pyplot(plt)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Season Classification</h3>

        <ul>
            <li><span style="font-weight:bold;">Summer:</span> March to June (hot and dry conditions).</li>
            <li><span style="font-weight:bold;">Monsoon:</span> July to mid-September (high humidity with heavy rainfall).</li>
            <li><span style="font-weight:bold;">Winter:</span> October to February (cold and dry conditions).</li>
        </ul>

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li><span style="font-weight:bold;">March to May</span> recorded the highest AQI levels across most locations.</li>
            <li><span style="font-weight:bold;">Dwarka</span>, <span style="font-weight:bold;">Okhla Phase III</span>, and <span style="font-weight:bold;">IGI Airport</span> showed extreme AQI spikes reaching nearly <span style="font-weight:bold;">450–480 AQI</span>.</li>
            <li><span style="font-weight:bold;">May</span> appears to be the peak pollution month overall.</li>
            <li><span style="font-weight:bold;">July and September</span> recorded the lowest AQI levels due to rainfall and monsoon effects.</li>
            <li>After <span style="font-weight:bold;">September</span>, AQI gradually increased again toward winter months.</li>
            <li><span style="font-weight:bold;">Anand Vihar</span>, <span style="font-weight:bold;">Rohini</span>, and <span style="font-weight:bold;">Connaught Place</span> maintained comparatively lower AQI levels than industrial and traffic-heavy regions.</li>
            <li>All locations followed a similar <span style="font-weight:bold;">seasonal pollution pattern</span>, showing that weather strongly influences air quality.</li>
            <li>The graphs indicate a sharp AQI increase before summer and a sharp decline during monsoon.</li>
        </ul>
        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li><span style="font-weight:bold;">Summer months</span> are the most polluted period in Delhi.</li>
            <li><span style="font-weight:bold;">Monsoon season</span> significantly improves air quality.</li>
            <li><span style="font-weight:bold;">Traffic-heavy</span> and <span style="font-weight:bold;">industrial zones</span> consistently experience worse AQI levels.</li>
        </ul>
        </div>
        <br>
    """, unsafe_allow_html=True)




# Q. Which Pollutants (PM2.5, PM10, NO₂, CO) Contribute Most to Poor Air Quality?

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                Q. Which Pollutants (PM2.5, PM10, NO₂, CO) Contribute Most to Poor Air Quality?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():
        plt.figure(figsize=(5,3))

        sns.heatmap(
            df[['aqi_index','pm2_5','pm10','co','no2']].corr(),
            annot=True
        )

        plt.title("Correlation Between AQI and Pollutants")

        st.pyplot(plt)

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li><span style="font-weight:bold;">AQI</span> and <span style="font-weight:bold;">PM10</span> have a strong positive correlation (<span style="font-weight:bold;">0.74</span>), indicating that PM10 is a major contributor to poor air quality.</li>
            <li><span style="font-weight:bold;">AQI</span> and <span style="font-weight:bold;">PM2.5</span> show a moderate positive correlation (<span style="font-weight:bold;">0.50</span>), meaning fine particulate matter also significantly affects AQI.</li>
            <li><span style="font-weight:bold;">PM2.5</span> and <span style="font-weight:bold;">PM10</span> are strongly correlated (<span style="font-weight:bold;">0.62</span>), showing that both pollutants often increase together.</li>
            <li><span style="font-weight:bold;">CO</span> and <span style="font-weight:bold;">NO₂</span> have a strong positive correlation (<span style="font-weight:bold;">0.73</span>), likely due to common sources such as vehicle emissions and fuel combustion.</li>
            <li><span style="font-weight:bold;">AQI</span> has a weak negative correlation with <span style="font-weight:bold;">CO</span> and <span style="font-weight:bold;">NO₂</span>, indicating that their direct influence on AQI is smaller compared to particulate matter.</li>
            <li><span style="font-weight:bold;">PM10</span> shows a slight negative relationship with <span style="font-weight:bold;">CO</span> and <span style="font-weight:bold;">NO₂</span>, suggesting that particulate pollution behaves differently from gaseous pollutants during certain periods.</li>
        </ul>

        <h3 class="h_container">Conclusion</h3>

        <ul>
            <li><span style="font-weight:bold;">Particulate matter (PM10 and PM2.5)</span> is the major driver of AQI deterioration in Delhi.</li>
            <li><span style="font-weight:bold;">Vehicle</span> and <span style="font-weight:bold;">combustion emissions</span> mainly influence CO and NO₂ levels together.</li>
            <li>Controlling <span style="font-weight:bold;">dust</span> and <span style="font-weight:bold;">particulate emissions</span> can significantly improve overall air quality.</li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)

# The Relationship Between PM10 and AQI Across Locations

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                The Relationship Between PM10 and AQI Across Locations
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():

        plt.figure(figsize=(16,7))

        scatter = sns.scatterplot(
            data=df,
            y='location',
            x=df['datetime'].dt.month_name(),
            hue='aqi_index',
            size='pm10',
            palette='seismic',
            sizes=(100, 2000),
            edgecolor=None
        )

        plt.xticks(rotation=45)

        plt.xlabel("Months")
        plt.ylabel("Locations")
        plt.title("Relationship Between PM10 and AQI Across Locations")

        st.pyplot(plt.gcf())

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li><span style="font-weight:bold;">March, April, and May</span> show the highest pollution levels across almost all locations.</li>
            <li><span style="font-weight:bold;">Dwarka</span>, <span style="font-weight:bold;">Okhla Phase III</span>, and <span style="font-weight:bold;">IGI Airport</span> are the most polluted locations, especially for <span style="font-weight:bold;">PM10</span>.</li>
            <li><span style="font-weight:bold;">PM10 concentration</span> is extremely high during March–May, indicating the impact of dust, construction activity, and dry weather conditions.</li>
            <li><span style="font-weight:bold;">June to August</span> show moderate pollution reduction due to rainfall and monsoon effects.</li>
            <li><span style="font-weight:bold;">September to November</span> recorded comparatively better AQI and lower PM10 levels.</li>
            <li><span style="font-weight:bold;">December and January</span> still show noticeable AQI levels because winter conditions trap pollutants near the ground.</li>
            <li><span style="font-weight:bold;">Connaught Place</span> and <span style="font-weight:bold;">Anand Vihar</span> maintain moderate pollution throughout the year but peak during summer.</li>
            <li><span style="font-weight:bold;">Rohini</span> has relatively balanced pollution levels compared to industrial and high-traffic zones.</li>
            <li>The graph clearly indicates a strong relationship between <span style="font-weight:bold;">PM10</span> and <span style="font-weight:bold;">AQI</span> — whenever PM10 increases, AQI also becomes severe.</li>
        </ul>
        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li><span style="font-weight:bold;">Summer months (March–May)</span> are the most critical pollution period in Delhi.</li>
            <li><span style="font-weight:bold;">Dwarka</span> and <span style="font-weight:bold;">Okhla Phase III</span> require stronger pollution control measures.</li>
            <li>The <span style="font-weight:bold;">monsoon season</span> significantly reduces particulate pollution levels.</li>
            <li><span style="font-weight:bold;">PM10</span> is one of the major contributors to AQI deterioration in Delhi.</li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">Feature Creation - AQI Category</h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():

        def aqi_categorize(aqi):

            if aqi < 50:
                return "Good"

            elif aqi <= 100:
                return "Satisfactory"

            elif aqi <= 200:
                return "Moderate"

            elif aqi <= 300:
                return "Poor"

            elif aqi <= 400:
                return "Very Poor"

            else:
                return "Severe"


        # Creating AQI categorical feature
        df['aqi_categorical'] = df['aqi_index'].apply(aqi_categorize)

        # AQI category order
        order = [
            'Good',
            'Satisfactory',
            'Moderate',
            'Poor',
            'Very Poor',
            'Severe'
        ]

        df.head()
df.head()


with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                How Frequently Does AQI Reach Unhealthy or Hazardous Levels?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():

        plt.figure(figsize=(14,6))

        a = sns.countplot(
            x=df['aqi_categorical'],
            order=order
        )

        for bars in a.containers:
            plt.bar_label(bars)

        plt.xlabel("AQI Categories")
        plt.ylabel("Count")
        plt.title("AQI Category Distribution")

        st.pyplot(plt.gcf())



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li>The majority of AQI records fall under the <span style="font-weight:bold;">Moderate</span> category (~33,663), showing that pollution levels are frequently above safe limits.</li>
            <li><span style="font-weight:bold;">Severe</span> AQI conditions were also observed frequently (~8,073), indicating recurring extreme pollution events.</li>
            <li><span style="font-weight:bold;">Poor</span> AQI levels occurred a significant number of times (~6,213), reflecting unhealthy air conditions.</li>
            <li><span style="font-weight:bold;">Very Poor</span> air quality was recorded around ~2,388 times.</li>
            <li><span style="font-weight:bold;">Satisfactory</span> AQI levels were comparatively low (~2,223), showing limited periods of cleaner air.</li>
            <li>The <span style="font-weight:bold;">Good</span> AQI category was almost absent, indicating that truly clean air conditions are very rare in the dataset.</li>
        </ul>

        <h3 class="h_container">Conclusion</h3>

        <ul>
            <li>Delhi experienced predominantly <span style="font-weight:bold;">Moderate to Severe</span> air quality conditions throughout the year.</li>
            <li><span style="font-weight:bold;">Clean air conditions</span> were extremely limited, highlighting persistent urban air pollution problems.</li>
        </ul>

        </div>
        <br>
    """, unsafe_allow_html=True)



with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
            <h2 class="h_container">
                What is the Percentage Contribution of Each AQI Category?
            </h2>
        </div>
        <br>
    """, unsafe_allow_html=True)

    with st.echo():

        aqi_pie = df['aqi_categorical'].value_counts()

        plt.figure(figsize=(2,2))

        plt.pie(
        x=aqi_pie.values,
        labels=aqi_pie.index,
        autopct='%1.1f%%',
        explode=[0,0.1,0.1,0.2,0],
        textprops={'fontsize':6}
        )

        plt.title("Percentage Distribution of AQI Categories")

        st.pyplot(plt.gcf())

with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">

        <h3 class="h_container">Key Insights</h3>

        <ul>
            <li><span style="font-weight:bold;">64%</span> of the AQI records fall under the <span style="font-weight:bold;">Moderate</span> category, making it the most dominant air quality condition.</li>
            <li>Around <span style="font-weight:bold;">15.4%</span> of the observations belong to the <span style="font-weight:bold;">Severe</span> category, indicating frequent extreme pollution conditions.</li>
            <li><span style="font-weight:bold;">11.8%</span> of the AQI levels fall under the <span style="font-weight:bold;">Poor</span> category.</li>
            <li><span style="font-weight:bold;">Very Poor</span> air quality contributes about <span style="font-weight:bold;">4.5%</span> of the total observations.</li>
            <li>Only <span style="font-weight:bold;">4.2%</span> of the records are classified as <span style="font-weight:bold;">Satisfactory</span>.</li>
            <li>The <span style="font-weight:bold;">Good</span> AQI category is nearly absent, showing that clean air conditions are extremely rare.</li>
        </ul>
        <h3 class="h_container">Conclusion</h3>
        <ul>
            <li>Most of Delhi’s air quality conditions remain in the <span style="font-weight:bold;">Moderate to Severe</span> range throughout the year.</li>
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