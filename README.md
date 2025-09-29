# Uber Fares Analysis 🚗📊

A comprehensive data analysis project examining Uber fare patterns, pricing trends, and geographical relationships using Python and data visualization techniques.

## 📋 Project Overview

This project analyzes Uber ride data to uncover insights about fare pricing, trip patterns, and geographical trends. The analysis includes data cleaning, feature engineering, geolocation processing, and exploratory data analysis with interactive visualizations.

## 🎯 Key Features

- **Data Preprocessing**: Cleaning and structuring raw Uber trip data
- **Geolocation Integration**: Converting coordinates to readable locations using Google Maps API
- **Distance Calculations**: Computing trip distances using the Haversine formula
- **Feature Engineering**: Creating time-based features and fare metrics
- **Exploratory Data Analysis**: Statistical analysis and data visualization
- **Outlier Detection**: Identifying and handling anomalous data points

## 📊 Dataset

The project uses Uber trip data with the following key features:
- Pickup and dropoff coordinates (latitude/longitude)
- Trip timestamps
- Fare amounts
- Passenger counts
- Trip distances (calculated)

**Dataset size**: ~200K records

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Plotly Express**: Interactive data visualizations
- **Google Maps API**: Reverse geocoding for location data
- **Jupyter Notebook**: Interactive development environment
- **Haversine Formula**: Geographic distance calculations

## 📁 Project Structure

```
Uber-Fares-Analysis/
├── uber-fares.ipynb           # Main analysis notebook
├── geolocation_google.py      # Google Maps API integration
├── haversine_function.py      # Distance calculation utilities
├── uber.csv                   # Raw Uber trip data
├── pickup_geocoded_results.csv # Geocoded location data
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Google Maps API key
- Required Python packages (see requirements.txt)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/necromet/Uber-Fares-Analysis.git
   cd Uber-Fares-Analysis
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
   ```

4. **Run the analysis**:
   Open `uber-fares.ipynb` in Jupyter Notebook or JupyterLab

### Required Packages

```python
pandas
numpy
plotly
requests
python-dotenv
jupyter
```

## 📈 Analysis Highlights

### Data Processing
- **Data Cleaning**: Renamed columns, handled missing values
- **Feature Engineering**: 
  - Extracted temporal features (year, month, day, hour, day of week)
  - Calculated fare per passenger metrics
  - Computed trip distances using Haversine formula

### Key Metrics Analyzed
- Fare amount distributions
- Trip distance patterns
- Passenger count analysis
- Temporal trends (hourly, daily, weekly patterns)
- Fare per passenger calculations

### Geolocation Processing
- Reverse geocoding of pickup coordinates
- Location-based fare analysis
- Geographic distribution of trips

### Outlier Handling
Applied quantile-based outlier detection (1st-99th percentile clipping) for:
- Fare amounts
- Passenger counts
- Trip distances
- Fare per passenger ratios

## 📊 Visualizations

The project includes interactive visualizations for:
- Fare amount distributions
- Trip distance histograms
- Temporal pattern analysis
- Passenger count distributions
- Geographic trip patterns

## 🔧 Key Functions

### `geolocation_google.py`
- `get_location(lat, lng)`: Reverse geocoding using Google Maps API

### `haversine_function.py`
- `haversine(lat1, lon1, lat2, lon2)`: Calculate distance between coordinates
- `calculate_bearing(lat1, lon1, lat2, lon2)`: Determine bearing between points
- `destination_point(lat1, lon1, distance_km, bearing_deg)`: Calculate destination coordinates

## 🚦 Usage Example

```python
import pandas as pd
from geolocation_google import get_location
from haversine_function import haversine

# Load data
df = pd.read_csv('uber.csv')

# Calculate trip distance
df['distance_km'] = df.apply(lambda row: haversine(
    row['pickup_latitude'], row['pickup_longitude'],
    row['dropoff_latitude'], row['dropoff_longitude']
), axis=1)

# Get location data (with API rate limiting)
location_data = get_location(40.7589, -73.9851)
```

## 🎯 Insights & Findings

- Identified optimal pricing patterns based on distance and time
- Discovered peak usage hours and fare variations
- Analyzed geographical hotspots for Uber usage
- Quantified relationship between distance and fare pricing

## 🙏 Acknowledgments

- Uber for providing the dataset
- Google Maps API for geolocation services
- The open-source community for the amazing Python libraries

## 📞 Contact

**Edward** - [@necromet](https://github.com/necromet)

Project Link: [https://github.com/necromet/Uber-Fares-Analysis](https://github.com/necromet/Uber-Fares-Analysis)
