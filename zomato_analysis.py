# -*- coding: utf-8 -*-
"""zomato_analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iFAKQJjn7xfQYOVLaVEyeFh2gJpWV2Yc

# Zomato Dataset Analysis
This notebook explores and analyzes restaurant data from Zomato to uncover meaningful insights.
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set visual style
sns.set(style='whitegrid')
# %matplotlib inline

# Load data
df = pd.read_csv('/content/zomato.csv', encoding='latin1')
df.head()

# Basic information
df.info()
df.describe(include='all')

# Check for missing values
df.isnull().sum()

# Drop rows with missing 'Cuisines'
df.dropna(subset=['Cuisines'], inplace=True)

# Convert relevant columns to appropriate types
df['Has Table booking'] = df['Has Table booking'].map({'Yes': 1, 'No': 0})
df['Has Online delivery'] = df['Has Online delivery'].map({'Yes': 1, 'No': 0})
df['Is delivering now'] = df['Is delivering now'].map({'Yes': 1, 'No': 0})
df.head()

# Rating distribution
plt.figure(figsize=(10,5))
sns.countplot(data=df, x='Aggregate rating', palette='coolwarm')
plt.title('Aggregate Rating Distribution')
plt.show()

# Votes vs Rating
plt.figure(figsize=(10,6))
sns.scatterplot(x='Aggregate rating', y='Votes', data=df, alpha=0.6)
plt.title('Votes vs Aggregate Rating')
plt.show()

# Cost for two vs Rating
plt.figure(figsize=(10,6))
sns.scatterplot(x='Average Cost for two', y='Aggregate rating', data=df, alpha=0.5)
plt.title('Cost for Two vs Rating')
plt.xscale('log')
plt.show()

# Top cuisines
top_cuisines = df['Cuisines'].value_counts().head(10)
top_cuisines.plot(kind='bar', figsize=(10,5), color='skyblue', title='Top 10 Cuisines')
plt.xticks(rotation=45)
plt.show()

# Most common cities
city_counts = df['City'].value_counts().head(10)
city_counts.plot(kind='bar', figsize=(10,5), color='coral', title='Top 10 Cities with Most Restaurants')
plt.xticks(rotation=45)
plt.show()

# Table booking impact
sns.boxplot(x='Has Table booking', y='Aggregate rating', data=df)
plt.title('Impact of Table Booking on Ratings')
plt.xticks([0, 1], ['No', 'Yes'])
plt.show()