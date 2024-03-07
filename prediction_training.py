# %% Importing the libraries
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

# %% Loading the data for analyzing

demand_data = pd.read_csv('C:/Users/linta/OneDrive/Desktop/Data Analytics Courses/Second Sem/DATA-406/Project/Data/Demand_Data.csv')
demand_data

# %%
gen_data = pd.read_csv('C:/Users/linta/OneDrive/Desktop/Data Analytics Courses/Second Sem/DATA-406/Project/Data/Generation_Data.csv')
gen_data

# %%  Data mining
demand_data.info()
# %%
demand_data.describe()

# %%
unique_regions = demand_data['Region'].unique()
unique_regions

# %% Count the number of unique regions
num_regions = len(unique_regions)
num_regions

# %% 
demand_data.columns
# %% 1. which region has the most hourly profile?

demand_data['Date'] = pd.to_datetime(demand_data['Date'], format='%d/%m/%Y')

season = 'WINTER'

filtered_data = demand_data[demand_data['Season'] == season]

# Aggregate hourly profiles by date and region
hourly_profile_count = filtered_data.groupby(['Date', 'Region', 'Hourly Profile']).size().unstack(fill_value=0)
# %% 

# Plot the results
plt.figure(figsize=(12, 8))
hourly_profile_count.plot(kind='line', marker='o', linestyle='-')
plt.title('Count of Hourly Profiles for All Regions in {}'.format(season))
plt.xlabel('Date')
plt.ylabel('Hourly Profile Count')
plt.xticks(rotation=45)
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

# %%
plt.figure(figsize=(12, 6))
sns.distplot(hourly_profile_count, bins=10, kde=True, hist_kws={'alpha': 0.5})
plt.title(f'Distribution of Hourly Profiles in {season} by Region')
plt.xlabel('Hourly Profile Count')
plt.ylabel('Density')
plt.legend(hourly_profile_count.columns)
plt.grid(True)
plt.tight_layout()
plt.show()

# %%

plt.figure(figsize=(10, 6))
hourly_profile_count.plot(kind='line', marker='o')
plt.title('Hourly Profile Count by Region in {}'.format(season))
plt.xlabel('Region')
plt.ylabel('Hourly Profile Count')
plt.xticks(rotation=45)
plt.legend(title='Hourly Profile', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# %% 2. Which fuel type is used mostly in all regions

total_generation_by_fuel = gen_data.groupby('Fuel Type')['Total Generation'].sum()

# Find the fuel type with the highest total generation
most_used_fuel_type = total_generation_by_fuel.idxmax()

print("Most used fuel type based on total generation:", most_used_fuel_type)

# %%
# Plot the results using a bar chart
plt.figure(figsize=(10, 6))
total_generation_by_fuel.plot(kind='area', color='skyblue')
plt.title('Total Generation by Fuel Type')
plt.xlabel('Fuel Type')
plt.ylabel('Total Generation')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()