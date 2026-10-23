import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px

st.set_page_config(
    page_title="Road Accidents in France | 2024",
    page_icon="🚗",
    layout="wide"
)

@st.cache_data
def load_data():
    path = Path(__file__).parent / "data" / "accidents_2024_clean.csv"
    data = pd.read_csv(path, parse_dates=["date"])
    return data

df = load_data()

# Dashboard header
st.title("Road Accidents in France — 2024")

st.markdown(
    """
    ### Understanding when, where, and under which conditions accidents occur

    This interactive dashboard explores **54,402 recorded road accidents**
    in France during 2024, using official French road accident data.

    The objective is to identify temporal, environmental, and geographical
    patterns while highlighting the limitations of accident frequency data.
    """
)

st.caption("Source: French Ministry of the Interior — BAAC 2024")

# ---------------------------------------
# DASHBOARD NAVIGATION
# ---------------------------------------

with st.sidebar:

    # EFREI Logo
    logo_path = Path(__file__).parent / "assets" / "Efrei_Logo_2026.svg"

    if logo_path.exists():
        st.image(str(logo_path), width=180)

    st.divider()

    st.header("Navigation")

    st.markdown("""
    - [Overview](#road-accidents-in-france-2024)
    - [Temporal Analysis](#temporal-analysis)
    - [Environmental Analysis](#environmental-analysis)
    - [Geographical Analysis](#geographical-analysis)
    - [Data Quality](#data-quality-and-limitations)
    - [Conclusions](#key-findings-and-conclusions)
    """)

    st.divider()

# Sidebar filters
st.sidebar.header("Dashboard Filters")

# Month dropdown filter
month_options = {
    "All months": 0,
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

selected_month = st.sidebar.selectbox(
    "Select month",
    options=list(month_options.keys())
)

month_value = month_options[selected_month]

selected_area = st.sidebar.selectbox(
    "Select area type",
    options=[
        "All areas",
        "Urban area",
        "Outside urban area"
    ]
)

# Apply filters
filtered_df = df.copy()

if month_value != 0:
    filtered_df = filtered_df[
        filtered_df["mois"] == month_value
    ]

if selected_area != "All areas":
    filtered_df = filtered_df[
        filtered_df["area_type"] == selected_area
    ]

# ---------------------------------------
# STUDENT & PROJECT INFORMATION
# ---------------------------------------

with st.sidebar:
    st.divider()

    logo_path = Path(__file__).parent / "assets" / "efrei_logo.png"

    if logo_path.exists():
        st.image(str(logo_path), width=160)

    st.markdown("### Student Information")

    st.markdown("""
    **Paul Moretti**

    **Program:** Bioinformatics

    **Year:** 4th Year (M1)

    **Institution:** EFREI Paris
    """)

    st.markdown(
        "**Email:** paul.moretti@efrei.net"
    )

    st.markdown(
        "**LinkedIn:** "
    )

    st.markdown(
        "**GitHub:** "
    )

    st.divider()

    st.markdown("### Project Information")

    st.markdown("""
    **Course:** Data Visualization & Storytelling

    **Project:** Road Accidents in France (2024)

    **Proposed by:** Prof. Mano Mathew
    """)

    st.markdown(
        "**Professor Contact:** "
        "[mano.mathew@efrei.fr](mailto:mano.mathew@efrei.fr)"
    )

# ---------------------------------------
# KEY PERFORMANCE INDICATORS
# ---------------------------------------

st.subheader("Key Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    label="Recorded Accidents",
    value=f"{len(filtered_df):,}",
    border=True
)

col2.metric(
    label="Urban Accidents",
    value=f"{(filtered_df['area_type'] == 'Urban area').sum():,}",
    border=True
)

col3.metric(
    label="Non-Urban Accidents",
    value=f"{(filtered_df['area_type'] == 'Outside urban area').sum():,}",
    border=True
)

st.divider()

with st.expander("Explore the Dataset"):
    st.dataframe(
        filtered_df.head(20),
        use_container_width=True
    )

# ---------------------------------------
# TEMPORAL ANALYSIS
# ---------------------------------------

st.subheader("Temporal Analysis")

st.markdown(
    "Explore how road accidents are distributed across months "
    "and hours of the day. All visualizations respond to the "
    "selected dashboard filters."
)

# Create two columns
chart1, chart2 = st.columns(2)

# Monthly / Daily Accident Distribution
with chart1:

    if selected_month == "All months":

        # Monthly distribution
        monthly_data = (
            filtered_df.groupby("mois")
            .size()
            .reset_index(name="Accidents")
        )

        fig_month = px.bar(
            monthly_data,
            x="mois",
            y="Accidents",
            title="Monthly Accident Distribution",
            labels={
                "mois": "Month",
                "Accidents": "Number of Accidents"
            }
        )

        fig_month.update_xaxes(
            tickmode="linear",
            dtick=1
        )

    else:

        # Daily distribution for the selected month
        daily_data = (
            filtered_df.groupby("jour")
            .size()
            .reset_index(name="Accidents")
        )

        fig_month = px.bar(
            daily_data,
            x="jour",
            y="Accidents",
            title=f"Daily Accident Distribution — {selected_month}",
            labels={
                "jour": "Day of the Month",
                "Accidents": "Number of Accidents"
            }
        )

        fig_month.update_xaxes(
            tickmode="linear",
            dtick=2
        )

    fig_month.update_layout(
        template="plotly_dark",
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(
        fig_month,
        use_container_width=True
    )

# Hourly accidents
with chart2:
    hourly_data = (
        filtered_df.groupby("hour")
        .size()
        .reset_index(name="Accidents")
    )

    fig_hour = px.bar(
        hourly_data,
        x="hour",
        y="Accidents",
        title="Hourly Accident Distribution",
        labels={
            "hour": "Hour of the Day",
            "Accidents": "Number of Accidents"
        }
    )

    fig_hour.update_layout(
        template="plotly_white",
        xaxis=dict(tickmode="linear", dtick=2),
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_hour, use_container_width=True)

# ---------------------------------------
# TEMPORAL INSIGHTS
# ---------------------------------------

if not filtered_df.empty:

    st.markdown("#### Key Temporal Insights")

    insight1, insight2 = st.columns(2)

    with insight1:
        if selected_month == "All months":
            peak_month = (
                filtered_df.groupby("mois")
                .size()
                .idxmax()
            )

            month_name = pd.Timestamp(
                year=2024, month=int(peak_month), day=1
            ).strftime("%B")

            st.info(
                f"**Monthly peak:** {month_name} recorded "
                f"the highest number of accidents within "
                f"the selected data."
            )
        else:
            peak_day = (
                filtered_df.groupby("jour")
                .size()
                .idxmax()
            )

            st.info(
                f"**Daily peak:** Day {peak_day} recorded "
                f"the highest number of accidents in "
                f"{selected_month}."
            )

    with insight2:
        peak_hour = (
            filtered_df.groupby("hour")
            .size()
            .idxmax()
        )

        st.info(
            f"**Hourly peak:** The highest number of "
            f"accidents occurred between "
            f"{int(peak_hour):02d}:00 and "
            f"{(int(peak_hour) + 1) % 24:02d}:00."
        )

    st.caption(
        "These findings describe accident frequency, "
        "not individual accident risk. Traffic exposure "
        "is not available in this dataset."
    )
else:
    st.info("No temporal insights available for the selected filters.")

# ---------------------------------------
# ENVIRONMENTAL ANALYSIS
# ---------------------------------------

st.divider()

st.subheader("Environmental Analysis")

st.markdown(
    "Explore the lighting and weather conditions under which "
    "road accidents were recorded in France in 2024."
)

# Create two columns
env1, env2 = st.columns(2)

# Lighting conditions
with env1:
    luminosity_data = (
        filtered_df.groupby("luminosity")
        .size()
        .reset_index(name="Accidents")
        .sort_values("Accidents", ascending=False)
    )

    fig_lum = px.bar(
        luminosity_data,
        x="luminosity",
        y="Accidents",
        title="Accidents by Lighting Conditions",
        labels={
            "luminosity": "Lighting Conditions",
            "Accidents": "Number of Accidents"
        },
        color_discrete_sequence=["#636EFA"]
    )

    fig_lum.update_layout(
        template="plotly_dark",
        xaxis_tickangle=-30,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_lum, use_container_width=True)


# Weather conditions
with env2:
    weather_data = (
        filtered_df.groupby("weather")
        .size()
        .reset_index(name="Accidents")
        .sort_values("Accidents", ascending=False)
    )

    fig_weather = px.bar(
        weather_data,
        x="weather",
        y="Accidents",
        title="Accidents by Weather Conditions",
        labels={
            "weather": "Weather Conditions",
            "Accidents": "Number of Accidents"
        },
        color_discrete_sequence=["#2E8B57"]
    )

    fig_weather.update_layout(
        template="plotly_dark",
        xaxis_tickangle=-30,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(fig_weather, use_container_width=True)

# ---------------------------------------
# ENVIRONMENTAL INSIGHTS
# ---------------------------------------

if not filtered_df.empty:

    st.markdown("#### Key Environmental Insights")

    insight3, insight4 = st.columns(2)

    # Lighting conditions insight
    with insight3:
        top_luminosity = (
            filtered_df["luminosity"]
            .value_counts()
        )

        luminosity_name = top_luminosity.idxmax()
        luminosity_count = top_luminosity.max()
        luminosity_percentage = (
            luminosity_count / len(filtered_df) * 100
        )

        st.info(
            f"**Most common lighting condition:** "
            f"{luminosity_name} accounts for "
            f"**{luminosity_percentage:.1f}%** of recorded "
            f"accidents ({luminosity_count:,} cases) "
            f"within the selected data."
        )

    # Weather conditions insight
    with insight4:
        top_weather = (
            filtered_df["weather"]
            .value_counts()
        )

        weather_name = top_weather.idxmax()
        weather_count = top_weather.max()
        weather_percentage = (
            weather_count / len(filtered_df) * 100
        )

        st.info(
            f"**Most common weather condition:** "
            f"{weather_name} accounts for "
            f"**{weather_percentage:.1f}%** of recorded "
            f"accidents ({weather_count:,} cases) "
            f"within the selected data."
        )

    st.caption(
        "These proportions describe the conditions under which "
        "accidents occurred. They do not measure the relative "
        "risk associated with lighting or weather conditions."
    )

else:
    st.info(
        "No environmental insights available for the selected filters."
    )

# ---------------------------------------
# GEOGRAPHICAL ANALYSIS
# ---------------------------------------

st.divider()

st.subheader("Geographical Analysis")

st.markdown(
    "Explore the distribution of recorded road accidents "
    "between urban and non-urban areas, and investigate "
    "their geographical locations using an interactive map."
)

# ---------------------------------------
# URBAN VS NON-URBAN DISTRIBUTION
# ---------------------------------------

area_data = (
    filtered_df.groupby("area_type")
    .size()
    .reset_index(name="Accidents")
)

if not area_data.empty:

    fig_area = px.pie(
        area_data,
        names="area_type",
        values="Accidents",
        hole=0.5,
        title="Urban vs Non-Urban Accidents",
        color="area_type",
        color_discrete_map={
            "Urban area": "#636EFA",
            "Outside urban area": "#2E8B57"
        }
    )

    fig_area.update_traces(
        textinfo="percent+label",
        hovertemplate=(
            "%{label}<br>"
            "Accidents: %{value:,}<br>"
            "Share: %{percent}<extra></extra>"
        )
    )

    fig_area.update_layout(
        template="plotly_dark",
        height=350,
        showlegend=False,
        margin=dict(l=10, r=10, t=50, b=10)
    )

    st.plotly_chart(
        fig_area,
        use_container_width=True
    )

else:
    st.warning("No accidents match the selected global filters.")


# ---------------------------------------
# GEOGRAPHICAL INSIGHTS
# ---------------------------------------

if not filtered_df.empty:

    st.markdown("#### Key Geographical Insights")

    urban_count = (
        filtered_df["area_type"] == "Urban area"
    ).sum()

    non_urban_count = (
        filtered_df["area_type"] == "Outside urban area"
    ).sum()

    total_accidents = len(filtered_df)

    urban_pct = urban_count / total_accidents * 100
    non_urban_pct = non_urban_count / total_accidents * 100

    if selected_area == "All areas":

        st.info(
            f"**Urban vs Non-Urban:** "
            f"{urban_pct:.1f}% of recorded accidents occurred "
            f"in urban areas, compared to "
            f"{non_urban_pct:.1f}% outside urban areas."
        )

    else:

        st.info(
            f"**Selected area:** {selected_area} accounts for "
            f"all {total_accidents:,} accidents currently "
            f"displayed in this geographical comparison."
        )

    st.caption(
        "Accident frequency does not measure relative road risk. "
        "Traffic exposure and accident severity are not included "
        "in this analysis."
    )

else:
    st.info(
        "No geographical insights available for the selected filters."
    )

# ---------------------------------------
# MAP-SPECIFIC FILTERS
# ---------------------------------------

st.markdown("### Interactive Accident Map")

st.caption(
    "These filters only affect the map. "
    "Global dashboard filters remain active."
)

map_col1, map_col2, map_col3, map_col4 = st.columns(4)

with map_col1:
    selected_day = st.selectbox(
        "Day of week",
        [
            "All days",
            "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"
        ]
    )

with map_col2:
    selected_hour = st.selectbox(
        "Hour of day",
        ["All hours"] + [
            f"{h:02d}:00" for h in range(24)
        ]
    )

with map_col3:
    selected_weather = st.selectbox(
        "Weather conditions",
        ["All weather"] + sorted(df["weather"].dropna().unique().tolist())
    )

with map_col4:
    selected_lighting = st.selectbox(
        "Lighting conditions",
        ["All lighting"] + sorted(df["luminosity"].dropna().unique().tolist())
    )

# Apply map-specific filters
map_filtered = filtered_df.copy()

if selected_day != "All days":
    map_filtered = map_filtered[
        map_filtered["day_of_week"] == selected_day
    ]

if selected_hour != "All hours":
    hour_value = int(selected_hour.split(":")[0])
    map_filtered = map_filtered[
        map_filtered["hour"] == hour_value
    ]

if selected_weather != "All weather":
    map_filtered = map_filtered[
        map_filtered["weather"] == selected_weather
    ]

if selected_lighting != "All lighting":
    map_filtered = map_filtered[
        map_filtered["luminosity"] == selected_lighting
    ]

# ---------------------------------------
# INTERACTIVE MAP
# ---------------------------------------

st.metric(
    "Accidents matching map filters",
    f"{len(map_filtered):,}"
)

# Prepare geographical data
map_display = map_filtered.dropna(
    subset=["lat", "long"]
).copy()

map_display = map_display[
    map_display["lat"].between(-90, 90) &
    map_display["long"].between(-180, 180)
]

if map_display.empty:
    st.warning(
        "No accidents match the selected filters. "
        "Try changing your selection."
    )

else:
    fig_map = px.scatter_map(
        map_display,
        lat="lat",
        lon="long",
        color="area_type",
        color_discrete_map={
            "Urban area": "#636EFA",
            "Outside urban area": "#2E8B57"
        },
        hover_data={
            "date": True,
            "hour": True,
            "weather": True,
            "luminosity": True,
            "lat": False,
            "long": False
        },
        center={"lat": 46.6, "lon": 2.2},
        zoom=4,
        height=650,
        title="Geographical Distribution of Road Accidents"
    )

# Adjust marker visibility according to the number of accidents
    n_accidents = len(map_display)

    if n_accidents > 20000:
        marker_size = 5
    elif n_accidents > 5000:
        marker_size = 7
    elif n_accidents > 1000:
        marker_size = 9
    else:
        marker_size = 13

    fig_map.update_traces(
        marker={
            "size": marker_size,
            "opacity": 1.0
        }
    )

    fig_map.update_layout(
        map_style="open-street-map",
        template="plotly_dark",
        legend_title="Area Type",
        margin=dict(l=0, r=0, t=50, b=0)
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )

st.caption(
    "Each point represents a recorded bodily injury accident. "
    "The map includes overseas territories, although its initial "
    "view is centered on metropolitan France."
)

# ---------------------------------------
# DATA QUALITY & LIMITATIONS
# ---------------------------------------

st.divider()

st.subheader("Data Quality & Limitations")

st.markdown(
    "Understanding data quality and methodological limitations "
    "is essential for interpreting the dashboard results correctly."
)

# Calculate data quality indicators using the complete dataset
total_records = len(df)
missing_addresses = df["adr"].isna().sum()
duplicate_records = df.duplicated(subset=["Num_Acc"]).sum()
unknown_collisions = df["collision_type"].eq("Unknown").sum()

# Data Quality KPI Cards
quality1, quality2, quality3, quality4 = st.columns(4)

quality1.metric(
    "Total Records",
    f"{total_records:,}",
    border=True
)

quality2.metric(
    "Missing Addresses",
    f"{missing_addresses:,}",
    border=True
)

quality3.metric(
    "Duplicate Accident IDs",
    f"{duplicate_records:,}",
    border=True
)

quality4.metric(
    "Unknown Collisions",
    f"{unknown_collisions:,}",
    border=True
)

st.caption(
    "Data quality indicators are calculated from the complete "
    "2024 dataset and are not affected by dashboard filters."
)

st.markdown("#### Data Preparation")

st.markdown(
    """
    - Converted geographical coordinates into numeric values.
    - Created date, hour, and day-of-week variables.
    - Decoded categorical variables using the official BAAC nomenclature.
    - Preserved accidents with missing addresses because geographical
      coordinates were available.
    - Classified six unspecified collision types as Unknown.
    - Checked duplicate accident identifiers and missing values.
    """
)

# ---------------------------------------
# METHODOLOGICAL LIMITATIONS
# ---------------------------------------

st.markdown("#### Methodological Limitations")

with st.expander("1. Accident Reporting and Dataset Coverage"):
    st.write(
        "The BAAC dataset contains bodily injury road accidents "
        "recorded by French law enforcement agencies. "
        "It does not include property-damage-only incidents, "
        "and some bodily injury accidents may not be reported "
        "or recorded. Therefore, the figures should not be "
        "interpreted as the total number of all road accidents."
    )

with st.expander("2. Traffic Exposure"):
    st.write(
        "The dataset does not provide traffic volumes, "
        "kilometers traveled, or the number of road users "
        "exposed to each condition. Consequently, accident "
        "counts cannot be directly interpreted as accident risk."
    )

with st.expander("3. Correlation and Causality"):
    st.write(
        "Observed differences across months, hours, weather, "
        "or lighting conditions do not establish causal "
        "relationships. Other factors, such as traffic density "
        "and driving behavior, may influence the results."
    )

with st.expander("4. Geographical Interpretation"):
    st.write(
        "The dataset includes metropolitan France and "
        "overseas territories. The map initially focuses on "
        "metropolitan France, but overseas accidents remain "
        "included in the analysis. Dense clusters of markers "
        "do not directly measure geographical accident risk."
    )

with st.expander("5. Accident Severity"):
    st.write(
        "This dashboard uses the accident characteristics file. "
        "It does not include individual injury outcomes. "
        "Therefore, the analysis focuses on recorded accident "
        "frequency rather than injury severity or fatalities."
    )

# ---------------------------------------
# KEY FINDINGS & CONCLUSIONS
# ---------------------------------------

st.divider()

st.subheader("Key Findings & Conclusions")

st.markdown(
    "The analysis of recorded road accidents in France in 2024 "
    "reveals several important temporal, environmental, "
    "and geographical patterns."
)

st.markdown("""
**1. Temporal Patterns**

July recorded the highest total number of accidents (5,209),
while June had the highest daily average (171.17 accidents/day).
The hourly distribution also revealed a pronounced peak
between 17:00 and 18:00.

**2. Environmental Conditions**

Most accidents were recorded during daylight (65.4%)
and under normal weather conditions (76.8%).
These proportions describe accident circumstances,
not the relative danger of these conditions.

**3. Geographical Distribution**

Urban areas accounted for 62.5% of recorded accidents,
compared with 37.5% outside urban areas.
The geographical map also highlights concentrations
around major urban centers.
""")

st.markdown("#### Implications & Recommendations")

st.markdown("""
- **Road safety planning:** Consider the observed temporal
  concentrations when prioritizing further investigations
  and potential prevention initiatives.

- **Local analysis:** Use geographical patterns to identify
  areas that may deserve more detailed examination.

- **Additional data:** Integrate traffic volume and injury
  severity data to better assess accident risk and consequences.

- **Further research:** Compare multiple years to determine
  whether the observed patterns persist over time.
""")

st.info(
    "Final takeaway: Road accidents are not uniformly distributed "
    "across time and space. However, accident frequency alone "
    "cannot establish relative risk or causality."
)
