"""""
Implement a custom function to categorize time of day into morning,
afternoon, evening, and night, and create a new column in the
DataFrame to store these categories. Use this new column to analyze
pedestrian activity patterns throughout the day.

-Students can also show plots analyzing activity.
"""""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ssl

# Function to ignore SSL certificate errors in URL
ssl._create_default_https_context = ssl._create_unverified_context

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Function to convert 'hour_beginning' column to datetime format
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')

# Function to categorize time of day
def categorize_time_of_day(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    elif 18 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

# Function to create a new 'time_of_day' column for all data
df['time_of_day'] = df['hour_beginning'].dt.hour.apply(categorize_time_of_day)

# Analysis of pedestrian activity by time of day for the entire dataset
activity_by_time_of_day = df.groupby('time_of_day')['Pedestrians'].mean()

# Plot of pedestrian activity by time of day
plt.figure(figsize=(8, 6))
sns.barplot(x=activity_by_time_of_day.index, y=activity_by_time_of_day.values, hue=activity_by_time_of_day.index, palette="viridis", legend=False  )
plt.title("Average Pedestrian Activity by Time of Day (All Data)")
plt.xlabel("Time of Day")
plt.ylabel("Average Number of Pedestrians")
plt.show()


