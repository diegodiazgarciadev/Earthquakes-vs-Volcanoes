import pandas as pd

#Loading first dataset
volcano_df = pd.read_csv("./data/volcano.csv")

# I keep the columns I think might be important
volcano_df = volcano_df[['volcano_number', 'volcano_name', 'primary_volcano_type', 'country',
 'region', 'subregion', 'latitude', 'longitude', 'elevation']]

volcano_df.to_pickle("./data/df_volcano_cleaned")

#Loading second dataset
eruptions_df = pd.read_csv("./data/eruptions.csv")

# I keep the columns I think might be important
# Looks like latitude and longitude might be important but we already have that information
# on the volcano dataset, and we are going to join the datasets soon
eruptions_df = eruptions_df[['volcano_number', 'volcano_name', 'eruption_number',
       'eruption_category', 'start_year',
       'start_month', 'start_day']]

#Eruption category catch my one from the first moment
#It is not very usefull but w can delete some rows

#I want information about the eruptions that took place without any doubt so
#I delete eruption_category== discredited eruption and Uncertain Eruption

eruptions_df = eruptions_df[(eruptions_df["eruption_category"]!="Discredited Eruption")]
eruptions_df = eruptions_df[(eruptions_df["eruption_category"]!="Uncertain Eruption")]

eruptions_df.to_pickle("./data/df_eruptions_cleaned")


#we are merging the volcano and the eruptions datasets
volc_erup_df = pd.merge(eruptions_df, volcano_df, on="volcano_number")


# We need all clean datas (most important on dates) so we will delete the Nans
#delete the start_yeaer null so that we can change the column year to int
volc_erup_df = volc_erup_df[(volc_erup_df["start_year"].isnull()==False)]
volc_erup_df = volc_erup_df[volc_erup_df['start_day'].isnull()==False]

# Looks like the date info are in float. Lets change those data types
volc_erup_df = volc_erup_df.astype({"start_year": int, "start_month": int, "start_day": int})

# Much better.
# We need to change the columns names start_year , start_month  and start_day to year, month , day
# I will create a new column Date using year, month and year .
# The method I will use need those names on the columns
volc_erup_df = volc_erup_df.rename(columns={'start_year': 'year','start_month': 'month','start_day': 'day'})

volc_erup_df.to_pickle("./data/df_volc_erup_df_cleaned")
