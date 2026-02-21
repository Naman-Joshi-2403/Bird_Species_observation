import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from dotenv import load_dotenv
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / "dev.env")
OUTPUT_PATH = os.path.join(BASE_DIR, os.getenv("CLEANED_DATA_PATH"))


st.set_page_config(
    page_title="Bird Species Observation Dashboard",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv(OUTPUT_PATH)

df = load_data()

with st.sidebar:
    selected = option_menu(
        menu_title="Bird Dashboard",
        options=[
            "Executive Overview",
            "Temporal Analysis",
            "Spatial Analysis",
            "Species Diversity",
            "Species Behavior",
            "Environmental Impact",
            "Distance Analysis",
            "Conservation Insights",
            "Observer Trends",
            "Advanced Analytics"
        ],
        menu_icon="globe",
        default_index=0,
    )

if selected == "Executive Overview":
    st.title("📊 Executive Overview")

    colf1, colf2 = st.columns(2)
    location = colf1.multiselect("Location Type",
                                 df["Location_Type"].unique(),
                                 default=df["Location_Type"].unique())
    year = colf2.multiselect("Year",
                             sorted(df["Year"].unique()),
                             default=sorted(df["Year"].unique()))

    filtered_df = df[
        (df["Location_Type"].isin(location)) &
        (df["Year"].isin(year))
    ]

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Observations", len(filtered_df))
    col2.metric("Unique Species", filtered_df["Scientific_Name"].nunique())
    col3.metric("Avg Temp", round(filtered_df["Temperature"].mean(), 2))
    col4.metric("Avg Humidity", round(filtered_df["Humidity"].mean(), 2))

    habitat_df = (
        filtered_df["Location_Type"]
        .value_counts()
        .reset_index(name="Count")
        .rename(columns={"index": "Location_Type"})
    )

    fig = px.bar(habitat_df,
                 x="Location_Type",
                 y="Count",
                 title="Observations by Habitat")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(habitat_df, hide_index=True)

elif selected == "Temporal Analysis":

    st.title("📅 Temporal Analysis")

    location = st.selectbox("Location Type",
                            df["Location_Type"].unique())

    filtered_df = df[df["Location_Type"] == location]

    yearly = filtered_df.groupby("Year").size().reset_index(name="Count")

    fig = px.line(yearly,
                  x="Year",
                  y="Count",
                  markers=True,
                  title="Year-wise Observation Trend")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(yearly, hide_index=True)

elif selected == "Spatial Analysis":

    st.title("🌍 Spatial Analysis")

    admin = st.multiselect("Admin Units",
                           df["Admin_Unit_Code"].unique(),
                           default=df["Admin_Unit_Code"].unique())

    filtered_df = df[df["Admin_Unit_Code"].isin(admin)]

    admin_df = (
        filtered_df["Admin_Unit_Code"]
        .value_counts()
        .reset_index(name="Count")
        .rename(columns={"index": "Admin_Unit_Code"})
    )

    fig = px.bar(admin_df,
                 x="Admin_Unit_Code",
                 y="Count",
                 title="Observations by Admin Unit")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(admin_df, hide_index=True)

elif selected == "Species Diversity":
    st.title("🐦 Species Diversity")

    habitat = st.radio("Habitat",
                       df["Location_Type"].unique())

    filtered_df = df[df["Location_Type"] == habitat]

    top_species_df = (
        filtered_df["Common_Name"]
        .value_counts()
        .head(20)
        .reset_index(name="Count")
        .rename(columns={"index": "Common_Name"})
    )

    fig = px.bar(top_species_df,
                 x="Common_Name",
                 y="Count",
                 title="Top 20 Observed Species")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(top_species_df, hide_index=True)

elif selected == "Species Behavior":

    st.title("🎵 Species Behavior")

    method = st.multiselect("ID Method",
                            df["ID_Method"].unique(),
                            default=df["ID_Method"].unique())

    filtered_df = df[df["ID_Method"].isin(method)]

    behavior_df = (
        filtered_df["ID_Method"]
        .value_counts()
        .reset_index(name="Count")
        .rename(columns={"index": "ID_Method"})
    )

    fig = px.pie(behavior_df,
                 names="ID_Method",
                 values="Count",
                 title="Identification Method Distribution")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(behavior_df, hide_index=True)

elif selected == "Environmental Impact":

    st.title("🌤 Environmental Impact")

    temp_range = st.slider(
        "Temperature Range",
        int(df["Temperature"].min()),
        int(df["Temperature"].max()),
        (int(df["Temperature"].min()), int(df["Temperature"].max()))
    )

    filtered_df = df[
        (df["Temperature"] >= temp_range[0]) &
        (df["Temperature"] <= temp_range[1])
    ]

    fig = px.scatter(filtered_df,
                     x="Temperature",
                     y="Humidity",
                     color="Location_Type",
                     title="Temperature vs Humidity")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(filtered_df.head(50), hide_index=True)

elif selected == "Distance Analysis":

    st.title("📏 Distance Analysis")

    species = st.selectbox("Species",
                           df["Common_Name"].unique())

    filtered_df = df[df["Common_Name"] == species]

    distance_df = (
        filtered_df["Distance"]
        .value_counts()
        .reset_index(name="Count")
        .rename(columns={"index": "Distance"})
    )

    fig = px.bar(distance_df,
                 x="Distance",
                 y="Count",
                 title="Distance Distribution")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(distance_df, hide_index=True)

elif selected == "Conservation Insights":
    st.title("🛡 Conservation Insights")

    habitat = st.selectbox("Habitat",
                           df["Location_Type"].unique())

    filtered_df = df[df["Location_Type"] == habitat]

    watchlist_df = (
        filtered_df["PIF_Watchlist_Status"]
        .value_counts()
        .reset_index(name="Count")
        .rename(columns={"index": "PIF_Watchlist_Status"})
    )

    fig = px.pie(watchlist_df,
                 names="PIF_Watchlist_Status",
                 values="Count",
                 title="Watchlist Status Distribution")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(watchlist_df, hide_index=True)


elif selected == "Observer Trends":

    st.title("👤 Observer Trends")

    observer_df = (
        df["Observer"]
        .value_counts()
        .head(15)
        .reset_index(name="Count")
        .rename(columns={"index": "Observer"})
    )

    fig = px.bar(observer_df,
                 x="Observer",
                 y="Count",
                 title="Top 15 Observers")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(observer_df, hide_index=True)

elif selected == "Advanced Analytics":

    st.title("📈 Advanced Analytics")

    pivot = df.pivot_table(
        values="Initial_Three_Min_Cnt",
        index="Location_Type",
        columns="Year",
        aggfunc="mean"
    )

    fig = px.imshow(pivot,
                    text_auto=True,
                    title="Avg Initial 3-Min Count Heatmap")

    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Supporting Dataset")
    st.dataframe(pivot, hide_index=True)