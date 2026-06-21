# 🌍 Decoding Delhi's Air Quality: AQI & Weather Analysis 2025

## 📌 Project Overview

Air pollution is one of the most critical environmental challenges affecting public health and urban sustainability. Delhi frequently experiences hazardous air quality levels due to vehicular emissions, industrial activities, construction dust, seasonal weather conditions, and population density.

This project analyzes Delhi's Air Quality Index (AQI) and weather conditions throughout 2025 to identify pollution patterns, seasonal trends, high-risk locations, and the influence of meteorological factors on air quality.

The analysis has been presented through an interactive Streamlit dashboard that allows users to explore insights, trends, conclusions, and recommendations.

---

## 🌐 Live Dashboard

🚀 Explore the project here:
https://srinivas-delhiweatheraqi.streamlit.app/

---

## 🎯 Problem Statement

Despite continuous environmental monitoring, pollution levels vary significantly across different locations and time periods in Delhi.

Understanding:

* When pollution peaks occur
* Which locations are most affected
* How weather conditions influence AQI
* Which pollutants contribute most to poor air quality

is essential for policymakers, environmental agencies, and citizens.

---

## 🎯 Objectives

* Perform comprehensive Exploratory Data Analysis (EDA) on Delhi AQI data.
* Study pollution trends across multiple locations.
* Analyze the impact of PM2.5, PM10, NO₂, and CO.
* Understand the relationship between weather and air pollution.
* Identify pollution hotspots and high-risk periods.
* Generate actionable recommendations for citizens and government authorities.

---

## 📊 Dataset Overview

The dataset contains hourly environmental and weather observations collected across multiple locations in Delhi during 2025.

### Features Included

| Category             | Features                                                       |
| -------------------- | -------------------------------------------------------------- |
| Location Information | Location, Latitude, Longitude                                  |
| Weather Information  | Temperature, Humidity, Pressure, Wind Speed, Weather Condition |
| Pollution Metrics    | AQI, PM2.5, PM10, CO, NO₂                                      |
| Time Features        | Date, Time, Datetime                                           |

---

## 🧹 Data Cleaning & Validation

Several data quality checks and preprocessing steps were performed:

### Data Cleaning Steps

* Converted Date and Time into a unified Datetime feature.
* Removed duplicate columns.
* Renamed columns for consistency.
* Rearranged features for improved readability.
* Validated pollutant ranges.
* Checked coordinate-location consistency.
* Verified weather category formatting.
* Verified humidity ranges.
* Identified and handled AQI values beyond CPCB standards.

### AQI Validation

According to CPCB standards:

* AQI Range = 0–500

During validation:

* 6,903 AQI values exceeded 500.
* These values were caused by extremely high pollutant concentrations.
* All values above 500 were clipped to 500 to maintain compliance with AQI guidelines.

### Data Quality Results

✅ No Missing Values

✅ No Duplicate Records

✅ No Invalid Coordinates

✅ No Negative Pollutant Measurements

✅ Consistent Weather Categories

---

## 📈 Analysis Modules

The Streamlit application contains multiple analysis sections:

### 🏠 Home

Project introduction and overview.

### 📘 About the Project

Project background, objectives, and methodology.

### 📊 Dataset Overview

Detailed explanation of the dataset and features.

### 🧹 Data Cleaning & Validation

Data preprocessing and quality assurance process.

### 📈 Pollution Trend Analysis

* AQI trend analysis
* Pollutant trend analysis
* Seasonal pollution patterns

### 🌦️ Weather Influence Analysis

Relationship between:

* Temperature and AQI
* Humidity and AQI
* Wind Speed and AQI
* Pressure and AQI

### 🕒 Time & Location Analysis

* Monthly AQI trends
* Hourly AQI trends
* Location-wise AQI comparison
* Pollution hotspot identification

### ⚠️ Public Alerts & Safety Tips

Health recommendations for citizens during high-pollution periods.

### 🏛️ Government Recommendations

Policy and environmental recommendations based on findings.

---

## 🔍 Key Insights

### Air Pollution Trends

* AQI levels fluctuate significantly throughout the year.
* Pollution peaks are observed during specific months and weather conditions.
* Several locations consistently exhibit higher pollution levels.

### Pollutant Impact

Among all pollutants:

* PM2.5 showed the strongest influence on AQI.
* PM10 significantly contributed to poor air quality.
* NO₂ and CO also affected pollution levels but with lower impact compared to particulate matter.

### Weather Influence

Weather conditions play a major role in AQI variation:

* Low wind speeds contribute to pollutant accumulation.
* Temperature inversions can worsen air quality.
* Humidity influences particulate matter concentration.
* Weather patterns affect pollutant dispersion.

### Location Analysis

Certain locations consistently reported:

* Higher AQI values
* Greater pollutant concentrations
* Increased health risk levels

making them critical pollution hotspots.

---

## ⚠️ Public Health Recommendations

Based on the analysis:

* Avoid outdoor activities during high AQI periods.
* Use N95/N99 masks in polluted regions.
* Limit outdoor exercise during severe pollution events.
* Monitor official AQI advisories.
* Use air purifiers indoors when pollution is severe.
* Encourage public transportation and carpooling.

---

## 🏛️ Government Recommendations

* Strengthen vehicular emission controls.
* Increase green belt development.
* Improve public transportation infrastructure.
* Control construction dust.
* Monitor industrial emissions more strictly.
* Deploy real-time pollution alert systems.
* Expand environmental awareness campaigns.

---

## 🛠️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Dashboard Development

* Streamlit

---

## 📂 Project Structure

```text
Delhi-AQI-Analysis/
│
├── app.py
├── pages/
│   ├── home.py
│   ├── about_project.py
│   ├── data_set_overview.py
│   ├── data_cleaning.py
│   ├── trend_analysis.py
│   ├── weather_influence.py
│   ├── time_location_analysis.py
│   ├── overall_conclusion.py
│   ├── alerts_for_people.py
│   ├── recommendations_govt.py
│   └── about_me.py
│
├── data/
│   └── DelhiWeatherAqi_2025.csv
│
├── assets/
│   └── explanation.mp4
│
├── requirements.txt
└── README.md
```

---

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Delhi-AQI-Analysis.git
```

Navigate to the project:

```bash
cd Delhi-AQI-Analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

### Pyarasani Srinivas

### Connect With Me

GitHub:
https://github.com/PYARASANISRINIVAS

LinkedIn:
https://www.linkedin.com/in/pya-srinivas/

---

## ⭐ Support

If you found this project useful, consider giving the repository a Star ⭐.

Feedback, suggestions, and contributions are welcome.
