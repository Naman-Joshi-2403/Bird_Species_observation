import os
import re
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / "dev.env")

FOREST_PATH = os.path.join(BASE_DIR , os.getenv("FOREST_DATA_PATH"))
GRASSLAND_PATH = os.path.join(BASE_DIR , os.getenv("GRASSLAND_DATA_PATH"))
OUTPUT_PATH = os.path.join(BASE_DIR , os.getenv("CLEANED_DATA_PATH"))


def process_interval_length(value):
    if pd.isna(value):
        return np.nan

    value = value.lower()

    match = re.search(r"(\d+\.?\d*)\s*[-–]\s*(\d+\.?\d*)", value)
    if match:
        low = float(match.group(1))
        high = float(match.group(2))
        return (low + high) / 2

    return np.nan

def process_distance(value):

    if pd.isna(value):
        return np.nan

    value = value.lower()

    # <= case
    match = re.search(r"<=\s*(\d+\.?\d*)", value)
    if match:
        return float(match.group(1)) / 2

    match = re.search(r"(\d+\.?\d*)\s*[-–]\s*(\d+\.?\d*)", value)
    if match:
        low = float(match.group(1))
        high = float(match.group(2))
        return (low + high) / 2

    # > case
    match = re.search(r">\s*(\d+\.?\d*)", value)
    if match:
        return float(match.group(1)) + 25

    return np.nan

def process_wind_category(value):
    if pd.isna(value):
        return "Unknown"

    value = value.lower()

    if "calm" in value:
        return "Calm"
    if "light air" in value:
        return "Light air movement"
    if "light breeze" in value:
        return "Light breeze"
    if "moderate breeze" in value:
        return "Moderate breeze"

    return "Other"

def process_wind_speed(value):
    if pd.isna(value):
        return np.nan

    value = value.lower()

    match = re.search(r"<\s*(\d+\.?\d*)\s*mph", value)
    if match:
        return float(match.group(1)) / 2

    match = re.search(r"(\d+\.?\d*)\s*[-–]\s*(\d+\.?\d*)\s*mph", value)
    if match:
        low = float(match.group(1))
        high = float(match.group(2))
        return (low + high) / 2

    match = re.search(r"(\d+\.?\d*)\s*mph", value)
    if match:
        return float(match.group(1))

    return np.nan

def load_and_merge():
    forest_sheets = pd.read_excel(FOREST_PATH, sheet_name=None)
    forest_df = pd.concat(forest_sheets.values(), ignore_index=True)
    forest_df["Ecosystem"] = "Forest"

    grassland_sheets = pd.read_excel(GRASSLAND_PATH, sheet_name=None)
    grassland_df = pd.concat(grassland_sheets.values(), ignore_index=True)
    grassland_df["Ecosystem"] = "Grassland"

    df = pd.concat([forest_df, grassland_df], ignore_index=True)

    return df

def clean_data(df):
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Year"] = pd.to_numeric(df["Year"], errors="coerce")

    df["Temperature"] = pd.to_numeric(df["Temperature"], errors="coerce")
    df["Humidity"] = pd.to_numeric(df["Humidity"], errors="coerce")

    df["Interval_Length_Minutes"] = df["Interval_Length"].apply(process_interval_length)

    df["Distance_Meters"] = df["Distance"].apply(process_distance)

    df["Wind_Category"] = df["Wind"].apply(process_wind_category)
    df["Wind_Speed_mph"] = df["Wind"].apply(process_wind_speed)

    df["Flyover_Observed"] = df["Flyover_Observed"].astype(str).str.upper()

    df = df.dropna(subset=["Scientific_Name", "Common_Name"])

    df = df.drop_duplicates()

    return df

if __name__ == "__main__":
    raw_df = load_and_merge()

    cleaned_df = clean_data(raw_df)

    cleaned_df.to_csv(OUTPUT_PATH, index=False)
