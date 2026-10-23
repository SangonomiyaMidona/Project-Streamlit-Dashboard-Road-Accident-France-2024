# Road Accidents in France — 2024
### Interactive Data Storytelling Dashboard with Streamlit

## 1. Project Overview

This project explores bodily injury road accidents recorded in France in 2024 through an interactive Streamlit dashboard.

### Main Research Question

**When, where, and under which conditions do road accidents occur in France?**

The objective is to identify temporal, environmental, and geographical patterns while highlighting the difference between recorded accident frequency and actual road risk.

The dashboard follows a data storytelling approach:

**Problem → Analysis → Insights → Implications**

### Target Audience

- Road safety authorities
- Local policymakers
- Researchers and data analysts
- Citizens interested in road safety

## 2. Dataset

The project uses official French road accident data.

- **Source:** French Ministry of the Interior — BAAC
- **Year:** 2024
- **Dataset:** Characteristics of bodily injury road accidents
- **Number of records:** 54,402
- **Original variables:** 15
- **Format:** CSV
- **Geographical coverage:** Metropolitan France and overseas territories

### Official Data Source

https://www.data.gouv.fr/datasets/bases-de-donnees-annuelles-des-accidents-corporels-de-la-circulation-routiere-annees-de-2005-a-2024

The dataset provides information about:

- Accident dates and times
- Geographical coordinates
- Lighting conditions
- Atmospheric conditions
- Urban and non-urban locations
- Intersection types
- Collision types

The original dataset is stored in `data/caract-2024.csv`.

The cleaned dataset used by the dashboard is stored in `data/accidents_2024_clean.csv`.

## 3. Data Exploration and Preparation

Data exploration and preprocessing were performed in Jupyter Notebook using Python and Pandas.

The complete analysis is available in `analysis.ipynb`.

### 3.1 Data Exploration

The initial exploration included:

- Dataset dimensions and variable types
- Missing values analysis
- Duplicate record detection
- Categorical variable validation
- Date and time consistency checks
- Geographical coordinate validation

### 3.2 Data Quality Results

| Indicator | Result |
|---|---|
| Total records | 54,402 |
| Original variables | 15 |
| Missing addresses | 2,310 (4.25%) |
| Duplicate accident IDs | 0 |
| Unknown collision types | 6 |

Missing addresses were preserved because geographical coordinates were available.

Unknown collision codes were classified as "Unknown" rather than removing the corresponding records.

### 3.3 Data Preprocessing

The following transformations were performed:

1. Converted geographical coordinates from decimal-comma strings to numeric values.
2. Created a date variable from day, month, and year.
3. Extracted accident hours from the original time variable.
4. Created a day-of-week variable.
5. Converted categorical codes into descriptive labels using the BAAC nomenclature.
6. Handled unknown collision categories.
7. Exported the cleaned dataset into a separate CSV file.

The original data was preserved to maintain traceability.

## 4. Dashboard Features

The interactive dashboard was developed with Streamlit and Plotly.

### 4.1 Dashboard Navigation

A sidebar navigation menu provides direct access to:

- Overview
- Temporal Analysis
- Environmental Analysis
- Geographical Analysis
- Data Quality
- Conclusions

### 4.2 Global Filters

Users can filter the dashboard by:

- Month
- Area type (urban or non-urban)

These filters automatically update the main indicators and visualizations.

### 4.3 Key Performance Indicators

The dashboard displays:

- Total recorded accidents
- Urban accidents
- Non-urban accidents

All three indicators respond to global filters.

### 4.4 Temporal Analysis

Interactive visualizations include:

- Monthly accident distribution
- Daily accident distribution when a specific month is selected
- Hourly accident distribution

The monthly visualization supports drill-down functionality, allowing users to explore individual days within a selected month.

Dynamic insights identify the periods with the highest recorded accident counts.

### 4.5 Environmental Analysis

The dashboard explores:

- Lighting conditions
- Weather conditions

Interactive bar charts display the distribution of recorded accidents across environmental categories.

Dynamic insights highlight the most common conditions within the selected data.

### 4.6 Geographical Analysis

The geographical section includes:

- Urban versus non-urban accident distribution
- Interactive geographical map
- Dynamic geographical insights

The map uses different colors to distinguish urban and non-urban accidents.

### 4.7 Map-Specific Filters

Additional filters apply exclusively to the interactive map:

- Day of the week
- Hour of the day
- Weather conditions
- Lighting conditions

These filters are cumulative and do not modify the other dashboard visualizations.

The map also displays the number of accidents matching the selected conditions.

Marker sizes adapt to the number of displayed accidents, improving readability.

## 5. Key Findings

The exploratory analysis revealed several important patterns.

### 5.1 Temporal Patterns

- July recorded the highest monthly total: 5,209 accidents.
- February recorded the lowest monthly total: 3,792 accidents.
- June had the highest daily average: 171.17 accidents per day.
- The highest hourly count occurred between 17:00 and 18:00, with 4,607 accidents.

The difference between monthly totals and daily averages demonstrates the importance of normalizing data when comparing periods of different lengths.

### 5.2 Environmental Conditions

- 65.40% of recorded accidents occurred during daylight.
- 76.84% occurred under normal weather conditions.

These results describe the circumstances in which accidents were recorded. They do not establish that favorable conditions are inherently more dangerous.

### 5.3 Geographical Distribution

- 62.52% of recorded accidents occurred in urban areas.
- 37.48% occurred outside urban areas.

The geographical visualization also highlights concentrations around major urban centers.

However, accident counts alone cannot establish geographical accident risk.

## 6. Methodological Limitations

Several limitations must be considered when interpreting the findings.

### 6.1 Reporting and Coverage

The BAAC database contains bodily injury road accidents recorded by French law enforcement agencies.

Property-damage-only accidents are excluded, and some bodily injury accidents may not be reported or recorded.

Consequently, the dataset does not represent every road incident occurring in France.

### 6.2 Traffic Exposure

The dataset does not provide:

- Traffic volumes
- Distances traveled
- Number of road users exposed to each condition

Accident frequency therefore cannot directly measure individual accident risk.

### 6.3 Correlation and Causality

Observed associations between accidents and environmental, temporal, or geographical conditions do not establish causal relationships.

Additional factors such as traffic density, driving behavior, and road infrastructure may influence accident occurrence.

### 6.4 Geographical Interpretation

The dataset covers metropolitan France and overseas territories.

The interactive map initially focuses on metropolitan France, but overseas records remain included.

Overlapping geographical markers can also make precise visual comparisons difficult.

### 6.5 Accident Severity

The dashboard uses the accident characteristics dataset.

It does not include individual injury outcomes, so the analysis focuses on recorded accident frequency rather than injury severity or fatalities.

## 7. Implications and Recommendations

The findings suggest several directions for further investigation.

### Road Safety Planning

Investigate periods with high recorded accident frequency, particularly late afternoon.

### Local Analysis

Use geographical patterns to identify locations where more detailed road safety investigations may be useful.

### Additional Data

Combine accident records with traffic exposure and injury severity data to support more meaningful risk assessments.

### Further Research

Compare multiple years to determine whether the patterns identified in 2024 remain consistent over time.

## 8. Installation and Usage

### 8.1 Requirements

The application uses Python and the following main libraries:

- Streamlit 1.51.0
- Pandas 2.3.3
- Plotly 6.3.0
- NumPy 2.3.4

The complete dependency list is available in `requirements.txt`.

### 8.2 Installation

Download or clone the project repository.

Open a terminal in the project directory.

Install the required dependencies:

```bash
python -m pip install -r requirements.txt
```

### 8.3 Launch the Dashboard

Run:

```bash
python -m streamlit run app.py
```

The application should open in your browser.

Default local address:

http://localhost:8501

### 8.4 Dataset Requirements

The application loads the cleaned CSV file from:

`data/accidents_2024_clean.csv`

Make sure this file is present before launching the dashboard.

The original data and preprocessing notebook are also provided for transparency and reproducibility.

## 9. Project Structure

```text
StApp26_20231187_MORETTI_BIO/
|
|-- app.py
|-- analysis.ipynb
|-- requirements.txt
|-- README.md
|
|-- data/
|   |-- caract-2024.csv
|   |-- accidents_2024_clean.csv
|
|-- assets/
    |-- Efrei_Logo_2026.svg
```

## 10. Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Plotly
- Streamlit
- Anaconda Navigator
- GitHub

## 11. Author and Academic Information

**Student:** Paul Moretti

**Institution:** EFREI Paris

**Program:** Bioinformatics

**Academic Year:** 4th Year (M1)

**Project:** Individual Student Project — Streamlit Dashboard

**Project proposed by:** Prof. Mano Mathew

**Professor contact:** mano.mathew@efrei.fr

## 12. Project Links

- **GitHub Repository:** (https://github.com/SangonomiyaMidona/Project-Streamlit-Dashboard-Road-Accident-France-2024)
- **Deployed Streamlit Application:** (https://project-app-dashboard-road-accident-france-2024-3uraj8pkioyjj2.streamlit.app/)
- **Demo Video:** https://youtu.be/1V1s1LxVTjY

## 13. Conclusion

This project demonstrates how interactive data visualization can support the exploration of road accident patterns.

The analysis reveals significant temporal, environmental, and geographical variations in recorded bodily injury accidents in France during 2024.

However, recorded accident frequency must not be confused with actual accident risk.

By combining data preparation, interactive visualization, and critical interpretation, the dashboard provides a foundation for further road safety analysis.

**Final takeaway: Understanding where and when accidents occur is an important first step, but understanding their causes and relative risks requires additional data.**
