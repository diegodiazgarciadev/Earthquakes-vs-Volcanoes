import pandas as pd
import src.CleaningFunctions as cf

df = pd.read_csv("./data/earthquake_ds.csv")
print("hola")
# I keep the columns I think might be importants
df_earthquakes = df[['Date', 'Time', 'Latitude', 'Longitude',
                   'Type', 'Depth', 'Magnitude']]

#we need to format the date for farther operations
df_earthquakes["Date"] = pd.to_datetime(df_earthquakes["Date"],utc=True).dt.strftime('%Y-%m-%d')
print(df_earthquakes)
#I create a new column Year from our Date column for using it in maps
try:
    df_earthquakes["Year"] = df_earthquakes["Date"].apply(cf.get_year)
except TypeError as err:
    print("type error", err)
print(df_earthquakes)

df_earthquakes.to_pickle("./data/df_earthquakes_cleaned")


