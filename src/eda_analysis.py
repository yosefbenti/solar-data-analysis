# eda_analysis.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset (ensure you specify the correct path)
data1 = pd.read_csv(r'D:\AI-10Academy\solar-data-analysis\data\benin-malanville.csv')
data2 = pd.read_csv(r'D:\AI-10Academy\solar-data-analysis\data\sierraleone-bumbuna.csv')
data3 = pd.read_csv(r'D:\AI-10Academy\solar-data-analysis\data\togo-dapaong_qc.csv')

# Display the first few rows of each DataFrame to check the structure
print("Benin Data (First 5 rows):")
print(data1.head())

print("\nSierra Leone Data (First 5 rows):")
print(data2.head())

print("\nTogo Data (First 5 rows):")
print(data3.head())

# 1. Summary Statistics
print("\nSummary Statistics:")
print(data1.describe())
print(data2.describe())
print(data3.describe())

# 2. Data Quality Check: Check for missing values and basic quality checks
print("\nMissing Values in Benin Data:")
print(data1.isnull().sum())
print("\nMissing Values in Sierra Leone Data:")
print(data2.isnull().sum())
print("\nMissing Values in Togo Data:")
print(data3.isnull().sum())

# Handle missing values by filling with zero or drop
data1.fillna(0, inplace=True)  # Or data1.dropna(inplace=True)
data2.fillna(0, inplace=True)
data3.fillna(0, inplace=True)

# 3. Time Series Analysis: Example for GHI over time (Assuming the timestamp is the same across all datasets)
plt.figure(figsize=(10, 6))
plt.plot(data1['timestamp'], data1['GHI'], label='Benin')
plt.plot(data2['timestamp'], data2['GHI'], label='Sierra Leone')
plt.plot(data3['timestamp'], data3['GHI'], label='Togo')
plt.title('Global Horizontal Irradiance (GHI) Over Time')
plt.xlabel('Time')
plt.ylabel('GHI')
plt.legend(loc='best')
plt.xticks(rotation=45)
plt.show()

# 4. Correlation Analysis: Correlation matrix for solar radiation and temperature (Benin data as example)
correlation_matrix_benin = data1[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']].corr()
sns.heatmap(correlation_matrix_benin, annot=True, cmap='coolwarm')
plt.title('Benin Data - Correlation Matrix')
plt.show()

# 5. Z-Score Analysis: Z-Score to detect outliers (Benin data as example)
from scipy.stats import zscore
z_scores_benin = np.abs(zscore(data1[['GHI', 'DNI', 'DHI', 'TModA', 'TModB']]))
outliers_benin = (z_scores_benin > 3)  # Threshold for outliers (z > 3 is considered an outlier)
print("\nOutliers in Benin Data (Z-Score > 3):")
print(outliers_benin)

# 6. Wind Analysis (Assuming wind data exists in the columns WS, WSgust, WD)
# Create a wind rose or radial plot for Wind Speed (WS) and Wind Gust (WSgust)
plt.figure(figsize=(10, 6))
sns.histplot(data1['WS'], kde=True, color='blue', label='Wind Speed (WS)')
sns.histplot(data1['WSgust'], kde=True, color='red', label='Wind Gust (WSgust)')
plt.title('Wind Speed and Wind Gust Distribution (Benin)')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Frequency')
plt.legend(loc='best')
plt.show()

# 7. Histogram for GHI, DNI, DHI, etc.
plt.figure(figsize=(10, 6))
sns.histplot(data1['GHI'], kde=True, color='orange', label='GHI')
sns.histplot(data1['DNI'], kde=True, color='green', label='DNI')
sns.histplot(data1['DHI'], kde=True, color='purple', label='DHI')
plt.title('Distribution of Solar Radiation (Benin Data)')
plt.xlabel('Solar Radiation')
plt.ylabel('Frequency')
plt.legend(loc='best')
plt.show()

# 8. Bubble Chart for GHI vs. TModA vs. WS (Wind Speed)
plt.figure(figsize=(10, 6))
plt.scatter(data1['GHI'], data1['TModA'], s=data1['WS']*10, alpha=0.5, c=data1['TModB'], cmap='viridis')
plt.title('GHI vs. Temperature vs. Wind Speed')
plt.xlabel('GHI')
plt.ylabel('Temperature (TModA)')
plt.colorbar(label='TModB')
plt.show()

# Continue with more tasks and analyses as required...
