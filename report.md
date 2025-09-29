# Uber Fares Analysis - Comprehensive Report

## Executive Summary

This report presents a comprehensive analysis of Uber ride data, examining fare patterns, operational insights, and pricing strategies. The analysis was conducted through two main components: data cleaning and exploratory data analysis (EDA). Key findings include evidence of dynamic pricing, strong correlation between distance and fare, and insights into seasonal and operational patterns.

## 1. Data Cleaning Process (`uber-fares-cleaning.ipynb`)

### 1.1 Initial Data Preparation

The data cleaning process began with loading the raw Uber dataset (`uber.csv`) containing 200,000 ride records. The initial steps included:

- **Column Renaming**: The unnamed index column was renamed to `fare_id` for better identification
- **Coordinate Rounding**: Pickup coordinates were rounded to 3 decimal places for efficient geocoding
- **Unique Location Identification**: Extracted unique pickup locations, reducing from 200,000 records to manageable geocoding targets

### 1.2 Feature Engineering

Several derived features were created to enhance the analysis:

#### Distance Calculation
- **Haversine Distance**: Calculated straight-line distance between pickup and dropoff points using the haversine formula
- **Distance Categories**: Classified trips into ranges (Short <2km, Medium 2-5km, Long 5-10km, etc.)

#### Temporal Features
- **Time Components**: Extracted year, month, day, hour, minute from pickup datetime
- **Day of Week**: Added day-of-week labels (Monday-Sunday) for pattern analysis
- **Time Periods**: Categorized hours into Night, Morning, Afternoon, and Evening

#### Pricing Metrics
- **Fare per Passenger**: Calculated individual passenger cost for group rides
- **Fare per Kilometer**: Distance-normalized pricing metric for efficiency analysis

### 1.3 Data Quality and Outlier Treatment

#### Outlier Management
Applied 1st and 99th percentile clipping to key variables:
- `fare_amount`
- `passenger_count` 
- `haversine_distance`
- `fare_per_passenger`

This approach removed extreme outliers while preserving data integrity, affecting approximately 2% of records.

#### Missing Data Handling
- Filled missing haversine distances with 0 (indicating same pickup/dropoff location)
- Applied geocoding to obtain location names from coordinates

### 1.4 Geocoding Integration

The cleaning process incorporated Google Maps API geocoding to:
- Convert lat/lng coordinates to readable location names
- Extract sublocality information (Manhattan, Brooklyn, Queens, etc.)
- Merge geographical context with ride data

**Final Output**: Clean dataset (`uber_cleaned.csv`) ready for comprehensive analysis

---

## 2. Exploratory Data Analysis (`uber-fares-analysis.ipynb`)

### 2.1 Business Performance Analysis

#### Peak Demand Patterns

**Hourly Demand Distribution:**
The heatmap analysis reveals clear demand patterns:
- **Peak Hours**: 18:00-20:00 (evening rush hour)
- **Secondary Peak**: 8:00-10:00 (morning rush hour)  
- **Low Demand**: 3:00-6:00 (early morning)
- **Weekend vs Weekday**: Distinct patterns with weekend demand shifted later

![Demand Heatmap](heatmap_visualization_would_be_here)

#### Location-Based Revenue Analysis

**Top Revenue Locations (by average fare):**
1. **Queens**: $29.34 average fare (9,661 trips)
2. **Staten Island**: $17.38 average fare (13 trips)
3. **Brooklyn**: $12.95 average fare (4,414 trips)
4. **Manhattan**: $10.21 average fare (181,151 trips)

**Key Insights:**
- Manhattan dominates by volume (90.5% of trips) but has lower average fares
- Queens generates highest per-trip revenue despite lower volume
- Staten Island shows premium pricing but minimal volume

### 2.2 Fare Variation Analysis

#### Distance-Fare Relationship
- **Strong Correlation**: 0.844 correlation between distance and fare
- **Linear Relationship**: Clear positive trend with some variance at longer distances
- **Pricing Efficiency**: Fare increases consistently with distance across all categories

#### Time-Based Fare Patterns
**Average Fare by Time Period:**
- **Night (0:00-6:00)**: $11.99
- **Morning (6:00-12:00)**: $10.97  
- **Afternoon (12:00-18:00)**: $11.45
- **Evening (18:00-24:00)**: $10.93

#### Passenger Count Impact
**Fare Efficiency by Group Size:**
- **1 Passenger**: $11.13 per person
- **2 Passengers**: $5.83 per person (-48% efficiency)
- **3 Passengers**: $3.79 per person (-66% efficiency)
- **6 Passengers**: $2.01 per person (-82% efficiency)

**Finding**: Clear economies of scale for group rides, making ride-sharing highly cost-effective.

### 2.3 Pricing Strategy Insights

#### Dynamic Pricing Evidence
**Statistical Analysis Results:**
- **ANOVA F-statistic**: 138.600 (p < 0.001)
- **Conclusion**: Significant evidence of dynamic pricing by hour
- **Peak Pricing**: 12:00 noon ($4.94/km) - highest rate
- **Low Pricing**: 5:00 AM ($3.60/km) - lowest rate
- **Price Variance**: 37% difference between peak and off-peak rates

#### Fare Anomalies and Outliers
- **Outlier Rate**: 8.6% of trips are statistical outliers
- **Fare Range**: $3.30 to $53.30 (after outlier treatment)
- **Distance Anomalies**: Some zero-distance trips with positive fares
- **Pricing Extremes**: 0.9% of rides have very high (>$20/km) or very low (<$1/km) per-km rates

### 2.4 Operational Pattern Analysis

#### Seasonal Trends
**Monthly Ridership Patterns:**
- **Peak Month**: May (18,859 trips)
- **Low Month**: August (14,221 trips)  
- **Seasonal Variation**: 9.7% coefficient of variation
- **Fare Stability**: Only 2.9% seasonal fare variation
- **Revenue Peak**: September ($11.66 average fare)

#### Trip Category Distribution
**Distance-Based Segmentation:**
- **Very Short (<2km)**: 44.4% of trips, 26.1% of revenue
- **Short (2-5km)**: 35.4% of trips, 34.4% of revenue
- **Medium (5-10km)**: 12.2% of trips, 21.8% of revenue
- **Long (10-20km)**: 3.7% of trips, 12.0% of revenue
- **Very Long (>20km)**: 1.4% of trips, 5.7% of revenue

**Key Finding**: Short trips (<5km) dominate operations (79.8% of all rides) but longer trips generate disproportionately higher revenue per trip.

### 2.5 Data Visualizations

The analysis includes several key visualizations:

1. **Demand Heatmap**: Hour-by-day trip volume patterns
2. **Fare vs Distance Scatter**: Shows linear relationship with variance
3. **Revenue by Location Bar Chart**: Compares average fares across pickup locations  
4. **Time Series Analysis**: Hourly fare variation demonstrating dynamic pricing
5. **Pricing Analysis Dashboard**: Four-panel view of pricing patterns
6. **Operational Patterns Dashboard**: Seasonal trends and trip categories

---

## 3. Key Business Insights

### 3.1 Revenue Optimization Opportunities

1. **Dynamic Pricing Effectiveness**: Clear evidence that time-based pricing is working, with 37% variation between peak and off-peak rates

2. **Location Strategy**: Focus on Queens and outer borough expansion could increase average fare revenue

3. **Group Ride Promotion**: Significant per-passenger savings (up to 82%) could drive adoption

### 3.2 Operational Efficiency

1. **Demand Prediction**: Clear hourly and seasonal patterns enable better driver allocation

2. **Short Trip Focus**: 79.8% of trips are under 5km, suggesting urban concentration strategy

3. **Peak Management**: Evening rush hour (6-8 PM) represents highest opportunity for surge pricing

### 3.3 Market Positioning

1. **Distance-Based Value**: Strong correlation (0.844) validates distance-based pricing model

2. **Seasonal Stability**: Low seasonal fare variation (2.9%) indicates stable pricing strategy

3. **Outlier Management**: 8.6% outlier rate suggests room for pricing algorithm improvements

---

## 4. Technical Implementation

### 4.1 Tools and Libraries Used
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **plotly**: Interactive visualizations
- **matplotlib/seaborn**: Statistical plotting
- **scipy**: Statistical testing (ANOVA)

### 4.2 Key Methodologies
- **Haversine Formula**: Accurate distance calculation accounting for Earth's curvature
- **Statistical Outlier Detection**: IQR method for identifying anomalous fares
- **Time Series Analysis**: Temporal pattern identification
- **Geospatial Analysis**: Location-based revenue insights
- **Correlation Analysis**: Relationship quantification between variables

### 4.3 Data Quality Measures
- **Outlier Treatment**: 1st-99th percentile clipping
- **Missing Value Handling**: Strategic imputation for distance calculations
- **Coordinate Precision**: 3-decimal place rounding for consistent geocoding
- **Validation**: Cross-validation of distance calculations and fare reasonableness

---

## 5. Conclusions and Recommendations

### 5.1 Strategic Recommendations

1. **Enhance Dynamic Pricing**: Expand time-based pricing to include day-of-week and seasonal factors

2. **Geographic Expansion**: Increase service in high-fare areas like Queens and Staten Island

3. **Group Ride Marketing**: Promote ride-sharing benefits with targeted campaigns highlighting cost savings

4. **Demand Management**: Implement predictive modeling for driver allocation based on identified patterns

### 5.2 Operational Improvements

1. **Outlier Investigation**: Develop automated systems to flag and investigate pricing anomalies

2. **Distance Validation**: Implement real-time route optimization to ensure accurate fare calculation

3. **Seasonal Adjustments**: Consider minor seasonal pricing adjustments despite current stability

### 5.3 Future Analysis Opportunities

1. **Route Optimization**: Analyze actual vs. straight-line distances for pricing accuracy
2. **Customer Segmentation**: Behavioral analysis based on trip patterns
3. **Competitor Analysis**: Market positioning relative to other ride-sharing services
4. **Weather Impact**: Correlation between weather conditions and demand/pricing

---

## 6. Data Sources and Limitations

### 6.1 Data Source
- **Primary Dataset**: uber.csv (200,000 ride records)
- **Geocoding**: Google Maps API integration
- **Time Period**: Full year coverage with monthly representation

### 6.2 Limitations
- **Geographic Coverage**: Primarily NYC metropolitan area
- **Route Accuracy**: Straight-line distances may not reflect actual routes
- **External Factors**: Weather, events, and traffic conditions not included
- **Customer Demographics**: No passenger demographic information available

### 6.3 Data Quality
- **Completeness**: >98% complete after cleaning
- **Accuracy**: Validated through statistical methods
- **Consistency**: Standardized formats and units throughout analysis

---

*Report Generated: September 2025*  
*Analysis Period: Full dataset year coverage*  
*Total Records Analyzed: ~200,000 Uber rides*