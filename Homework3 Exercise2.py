'''
Track pedestrian counts on the Brooklyn Bridge for the year 2019 and analyze how different weather conditions influence pedestrian
activity in that year. Sort the pedestrian count data by weather summary to identify any correlations( with a correlation matrix)
between weather patterns and pedestrian counts for the selected year.

-This question requires you to show the relationship between a numerical feature(Pedestrians) and a non-numerical feature(Weather
Summary). In such instances we use Encoding. Each weather condition can be encoded as numbers( 0,1,2..). This technique is called One-hot
encoding.

-Correlation matrices may not always be the most suitable visualization method for relationships involving categorical
datapoints, nonetheless this was given as a question to help you understand the concept better.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore
import ssl

# Ignore SSL certificate errors
ssl._create_default_https_context = ssl._create_unverified_context

# Read the dataset
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

# Convert 'hour_beginning' column to datetime format
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], format='%m/%d/%Y %I:%M:%S %p')

# Filter for data in 2019
df_2019 = df[df['hour_beginning'].dt.year == 2019].copy()

# One-hot encode the 'Weather Summary' column
df_encoded = pd.get_dummies(df_2019, columns=['weather_summary'])

# Selecting only the Pedestrians column and one-hot encoded weather columns
columns_of_interest = ['Pedestrians'] + [col for col in df_encoded.columns if col.startswith('weather_summary')]
df_selected = df_encoded[columns_of_interest]

# Correlation matrix for Pedestrians vs weather conditions summary
corr_matrix = df_selected.corr()

# Heatmap for Pedestrians vs weather conditions summary
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix[['Pedestrians']].sort_values(by='Pedestrians', ascending=False), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation between Pedestrian Counts and Weather Conditions in 2019")
plt.show()