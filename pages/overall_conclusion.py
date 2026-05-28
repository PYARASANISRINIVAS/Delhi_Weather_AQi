
import streamlit as st 
with st.container():
    st.markdown("""
        <div class="custom-box" style="border-radius: 5px;">
        <h2 class="h_container">
            Overall Conclusion
        </h2>
        <ul>
            <li>
                The analysis shows that <span style="font-weight:bold;">AQI levels vary strongly with seasonal and weather changes</span> across all Delhi locations.
            </li>
            <li>
                <span style="font-weight:bold;">March, April, and May</span> recorded the highest AQI values, indicating severe pollution during pre-summer and summer months.
            </li>
            <li>
                <span style="font-weight:bold;">July and September</span> showed the lowest AQI levels, suggesting that monsoon conditions help reduce pollution concentration.
            </li>
            <li>
                <span style="font-weight:bold;">Dwarka</span>, <span style="font-weight:bold;">Okhla Phase III</span>, and <span style="font-weight:bold;">IGI Airport</span> consistently showed higher AQI and PM10 levels compared to other locations.
            </li>
            <li>
                <span style="font-weight:bold;">PM10</span> had the strongest positive correlation with AQI (<span style="font-weight:bold;">0.74</span>), making it the most influential pollutant in overall air quality deterioration.
            </li>
            <li>
                <span style="font-weight:bold;">PM2.5</span> also showed a moderate positive relationship with AQI (<span style="font-weight:bold;">0.50</span>), contributing significantly to pollution levels.
            </li>
            <li>
                <span style="font-weight:bold;">NO₂</span> and <span style="font-weight:bold;">CO</span> were strongly correlated (<span style="font-weight:bold;">0.73</span>), indicating that both pollutants likely originate from similar emission sources.
            </li>
            <li>
                Weather conditions significantly affected AQI:
                <ul>
                    <li>
                        <span style="font-weight:bold;">Clear sky</span> and <span style="font-weight:bold;">fog conditions</span> showed higher AQI values.
                    </li>
                    <li>
                        <span style="font-weight:bold;">Rain</span> and <span style="font-weight:bold;">drizzle conditions</span> showed noticeably lower AQI values.
                    </li>
                    <li>
                        <span style="font-weight:bold;">Heavy rain</span> and <span style="font-weight:bold;">light drizzle</span> weather were associated with the cleanest air conditions in the dataset.
                    </li>
                </ul>
            </li>
            <li>
                <span style="font-weight:bold;">Humidity</span> showed a negative correlation with AQI (<span style="font-weight:bold;">-0.42</span>), meaning increased moisture levels were associated with lower pollution.
            </li>
            <li>
                <span style="font-weight:bold;">Temperature</span> had only a weak positive relationship with AQI (<span style="font-weight:bold;">0.23</span>), indicating limited direct influence.
            </li>
            <li>
                <span style="font-weight:bold;">Higher wind speeds</span> helped reduce gaseous pollutants like CO and NO₂ by dispersing pollutants more effectively.
            </li>
            <li>
                <span style="font-weight:bold;">Industrial zones</span> recorded the highest pollution levels among residential, commercial, and industrial regions.
            </li>
            <li>
                Pollution levels consistently increased from:
                <br>
                <span style="font-weight:bold;">
                    Residential → Commercial → Industrial zones
                </span>
            </li>
            <li>
                <span style="font-weight:bold;">CO</span> was identified as the dominant pollutant across most zones.
            </li>
            <li>
                Clear sky weather was the most frequently observed weather condition across all locations, supporting pollution accumulation.
            </li>
            <li>
                Rainfall events were comparatively limited, reducing natural pollutant cleansing opportunities.
            </li>
            <li>
                Hourly trends showed AQI remaining relatively stable throughout the day, with a slight increase during evening hours.
            </li>
            <li>
                The <span style="font-weight:bold;">highest AQI levels</span> were observed during evening peak traffic hours around <span style="font-weight:bold;">6 PM to 7 PM</span>.
            </li>
            <li>
                Weekly analysis showed only small AQI variations across days, indicating pollution persists consistently throughout the week.
            </li>
            <li>
                <span style="font-weight:bold;">Saturday</span> recorded comparatively higher AQI levels than other weekdays.
            </li>
            <li>
                All monitored locations followed a similar annual pollution pattern, showing that <span style="font-weight:bold;">seasonal weather changes strongly influence Delhi’s air quality.</span>
            </li>
            <li>
                Overall, the analysis indicates that:
                <br>
                <span style="font-weight:bold;">
                    particulate matter pollution, traffic emissions, industrial activity, and seasonal weather conditions
                </span>
                are the major factors affecting Delhi’s air quality.
            </li>
        </ul>
        </div>
        <br>
    """, unsafe_allow_html=True)