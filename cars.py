
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

cars_df = pd.read_csv('cars.csv')
print(cars_df)

print(cars_df.info())

print(cars_df.head(10))
print(cars_df.tail(10))
print(cars_df.columns)
print(cars_df.isnull().sum())
print(cars_df.describe())

cars_df["MSRP"] = cars_df["MSRP"].str.replace("$", "")
cars_df["MSRP"] = cars_df["MSRP"].str.replace(",", "")
cars_df["MSRP"] = cars_df["MSRP"].astype(int)
print(cars_df["MSRP"])
cars_df["Invoice"] = cars_df["Invoice"].str.replace("$", "")
cars_df["Invoice"] = cars_df["Invoice"].str.replace(",", "")
cars_df["Invoice"] = cars_df["Invoice"].astype(int)
print(cars_df["Invoice"])

print(cars_df.head())

print(cars_df.info())

fig = px.scatter_matrix(cars_df, width = 1500, height = 1500)
fig.show()

sns.pairplot(data = cars_df) 
plt.show()

fig = px.scatter(cars_df, x = 'Horsepower', y = 'MSRP', text = 'Make', color = 'Cylinders', hover_name = 'Cylinders')
fig.update_traces(textposition = "top center")
fig.show()


print(cars_df.Make.unique())

fig = px.histogram(cars_df, x = 'Make', title = 'Car Makers')
fig.show()


fig = px.histogram(cars_df, x = 'Type', title = 'Car Models', color = 'Make', height = 700, width = 900)
fig.show()

print(cars_df[cars_df['Type'] == 'Sports'])


fig = px.imshow(cars_df.corr(), height = 700)
fig.show()


corr_matrix = cars_df.corr()
corr_matrix
sns.heatmap(corr_matrix, annot = True)
fig.show()











