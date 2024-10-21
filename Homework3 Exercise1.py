"""""
1. Filter the data to include only weekdays (Monday to Friday) and
plot a line graph showing the pedestrian counts for each day of the
week.
import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)
"""""

import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import ssl

# Ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Convert 'hour_beginning' column to datetime format
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')

# Filter for weekdays
df_weekdays = df[df['hour_beginning'].dt.dayofweek < 5].copy()  # Monday to Friday

# Group by day of the week and sum pedestrian counts
df_weekdays.loc[:, 'day_of_week'] = df_weekdays['hour_beginning'].dt.day_name()  # Get the day name
pedestrian_counts = df_weekdays.groupby('day_of_week')['Pedestrians'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])

# Plot the data
plt.figure(figsize=(10, 6))
pedestrian_counts.plot(kind='bar', color='orange')
plt.title('Total Pedestrian Counts per Day of the Week')
plt.xlabel('Day of the Week')
plt.ylabel('Total Pedestrian Count')
plt.xticks(rotation=45)
plt.grid(axis='y')  # Only show gridlines for the y-axis
plt.show()

