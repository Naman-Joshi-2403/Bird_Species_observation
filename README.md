# 🐦 Bird Species Observation Analysis

## Forest & Grassland Ecosystem Study

------------------------------------------------------------------------

## 📌 Project Overview

This project analyzes bird species observations across **Forest** and
**Grassland** ecosystems to understand:

-   Species distribution patterns
-   Habitat preferences
-   Environmental impact on bird activity
-   Conservation priority trends

The project follows a structured workflow:

Data Cleaning → EDA → Visualization → Insights

------------------------------------------------------------------------

# 🗂️ Actual Project Structure

    BIRD_SPECIES_OBSERVATION/
    │
    ├── Code/
    │   ├── dashboard.py 
    │   └── data_cleaning.py 
    │
    ├── Input/
    │   ├── Bird_Monitoring_Data_FOREST.XLSX
    │   └── Bird_Monitoring_Data_GRASSLAND.XLSX
    │
    ├── Output/
    │   └── cleaned_bird_data.csv
    ├── env/                     
    │
    ├── dev.env                  
    ├── requirement.txt          
    └── README.md

------------------------------------------------------------------------

# ⚙️ Tech Stack

-   Python
-   Pandas
-   NumPy
-   Plotly
-   Streamlit

------------------------------------------------------------------------

# 🚀 Setup Instructions

Follow these steps to run the project locally.

------------------------------------------------------------------------

## 1️⃣ Clone the Repository

``` bash
git clone https://github.com/Naman-Joshi-2403/Bird_Species_observation.git
cd Bird_Species_observation
```

------------------------------------------------------------------------

## 2️⃣ Create Virtual Environment

### Windows

``` bash
python -m venv env
env\Scripts\activate
```

------------------------------------------------------------------------

## 3️⃣ Install Dependencies

``` bash
pip install -r requirement.txt
```

------------------------------------------------------------------------

## 4️⃣ Configure Environment Variables

Make sure your `dev.env` file contains the correct paths:

    FOREST_DATA_PATH=Input/Bird_Monitoring_Data_FOREST.XLSX
    GRASSLAND_DATA_PATH=Input/Bird_Monitoring_Data_GRASSLAND.XLSX
    OUTPUT_PATH=Output/cleaned_bird_data.csv

------------------------------------------------------------------------

## 5️⃣ Run Data Cleaning Script

This step consolidates and cleans the multi-sheet Excel data.

``` bash
python Code/data_cleaning.py
```

This will generate:

    Output/cleaned_bird_data.csv

------------------------------------------------------------------------

## 6️⃣ Run Streamlit Dashboard

``` bash
streamlit run Code/dashboard.py
```

The app will open in your browser at:

    http://localhost:8501

------------------------------------------------------------------------

# 📊 Analysis Performed

## 🔹 Data Cleaning

-   Multi-sheet Excel handling
-   Missing value treatment
-   Column formatting & standardization
-   Date-time transformation
-   Habitat consolidation (Forest vs Grassland)

## 🔹 Exploratory Data Analysis

-   Temporal trends (Year / Month)
-   Spatial distribution (Plot / Location Type)
-   Species diversity metrics
-   Environmental correlation (Temperature, Humidity, Wind)
-   Observer trend analysis
-   Conservation watchlist insights

## 🔹 Dashboard Features

-   Habitat filter (Forest / Grassland)
-   Species-level analysis
-   Year-wise trends
-   Environmental impact visualization
-   Interactive Plotly charts

------------------------------------------------------------------------

# 📌 Key Insights Generated

-   Habitat-specific species richness
-   Seasonal bird activity peaks
-   High biodiversity plots
-   Environmental factor influence on bird sightings
-   At-risk species identification

------------------------------------------------------------------------

# 📦 Deliverables

✔ Cleaned Dataset (`cleaned_bird_data.csv`)\
✔ Python Source Code\
✔ Interactive Streamlit Dashboard\
✔ Structured Project Documentation

------------------------------------------------------------------------

# 🧠 Future Enhancements

-   Add machine learning model for species prediction
-   Deploy Streamlit app to cloud (Render / AWS / Streamlit Cloud)
-   Add geographic mapping with coordinates
-   SQL database integration for large-scale storage

------------------------------------------------------------------------

# 👨‍💻 Author

Naman Joshi

------------------------------------------------------------------------

⭐ If you found this project helpful, consider giving the repository a
star!
