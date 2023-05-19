import pandas as pd 
import plotly.express as px
import numpy as np 
import matplotlib as plt  
import seaborn as sns 

#to read the file
cars_df = pd.read_csv(r'C:/Users/abyak/OneDrive\Desktop/MyProject/cars.csv')
print (cars_df)

# to check top rows
cars_df.head(10)

#to check bottom rows
cars_df.tail(10)

#to check columns
cars_df.columns

#to obtain the statistical summary of the dataframe
cars_df.describe()

cars_df["MSRP"] = cars_df["MSRP"].str.replace("$", "")
cars_df["MSRP"] = cars_df["MSRP"].str.replace(",", "")
cars_df["MSRP"] = cars_df["MSRP"].astype(int)

print(cars_df["MSRP"])

cars_df["Invoice"] = cars_df["Invoice"].str.replace("$", "")
cars_df["Invoice"] = cars_df["Invoice"].str.replace(",", "")
cars_df["Invoice"] = cars_df["Invoice"].astype(int) 

print(cars_df['Invoice'])


fig = px.scatter_matrix(cars_df, width = 1500, height = 1500)
fig.show()




