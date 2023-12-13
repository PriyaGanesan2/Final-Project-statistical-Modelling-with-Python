import requests
import pandas as pd
import os # use this to access your environment variables
from citybikes import get_city_bikes_info
from apicall import get_venues_fs,query_yelp
import json

FOURSQUARE_KEY = os.environ['FOURSQUARE_KEY']
foursquare_api_key = "FOURSQUARE_KEY"
YELP_KEY = os.environ['YELP_KEY']
yelp_api_key="2txPFbV_tXJZkf8zylCHxgz4lKx2c8SDNTUwCrHr93uHVHj53ht4KlNmECmIRISmpkmKfdMGjRmsYqnOsBpdMSjs698QU0jbGgxn3DHZ2YFum1YFTtkFKJ3FbLJuZXYx"
network_id="bixi-toronto"
foursquare_df = pd.DataFrame(columns=["category","open","name", "address", "city"])
yelp_df = pd.DataFrame(columns=["category","open","name", "address", "city"])
df_four=pd.DataFrame()
df_yelp=pd.DataFrame()
# Your tasks are as follows:
# 1. Connect to the  [Foursquare](https://developer.foursquare.com/places) API
# 2. Connect to the [Yelp](https://www.yelp.com/developers/documentation/v3/get_started) API. This API offers similar services as Foursquare.
# 3. For each of the bike stations in Part 1, query both APIs to retrieve information for the following in that location:
#  - Restaurants or bars
#  - Various POIs (points of interest) of your choice
# 4. Create a DataFrame for the Yelp results and Foursquare results. 
# 5. Compare the quality of the Yelp and Foursquare API. For your location, which API gives you the most complete information/better coverage? *NOTE:* Your definition of 'coverage' is up to you. It could be simple 'number of POIs in the area', but it could also be something more specific like 'number of reviews per POI', or 'number of different attributes of each POI'.


#call citybikes to fecth location details for all sations in the selected city 
# bike_info_df=get_city_bikes_info(network_id)
# bike_info_df=bike_info_df[(bike_info_df.latitude.notna()) & (bike_info_df.longitude.notna())]

# I have ran this api call to fetch citybikes station , lat, log and saved it to a csv file. 
# fetching info for this from csv file
file_path = '/Users/priyaganesan/Desktop/python_exercise/Pandas_exercise/db/Final-Project-statistical-Modelling-with-Python/bike_info_csv.csv'

# Read the CSV file into a DataFrame
bike_info_df = pd.read_csv(file_path)

point_of_interest_coordinates = bike_info_df[['latitude', 'longitude']]
#test with 5 records and then commnt this out and save the results in csv
#point_of_interest_coordinates=point_of_interest_coordinates.head(5)
#print(point_of_interest_coordinates)

# for each station lat,long call foursquare and yelp
for index, row in point_of_interest_coordinates.iterrows():
    latitude = row['latitude']
    longitude = row['longitude']
    # Call function to fetch points of interest near each lat,long from foursquare ,12080-library,14010-christmas market
    #13065 - resturant,16019-hiking trails,16032-park
    y_res=query_yelp(latitude,longitude,yelp_api_key)
    f_res=get_venues_fs(latitude,longitude,1000,FOURSQUARE_KEY,'13065,16032,12080') 
    
    # Append the new DataFrame to the existing DataFrame
    df_four = pd.concat([df_four, f_res], ignore_index=True)
    df_yelp = pd.concat([df_yelp, y_res], ignore_index=True)

df_four.to_csv('/Users/priyaganesan/Desktop/python_exercise/Pandas_exercise/db/Final-Project-statistical-Modelling-with-Python/df_four_csv.csv', index=False)  
df_yelp.to_csv('/Users/priyaganesan/Desktop/python_exercise/Pandas_exercise/db/Final-Project-statistical-Modelling-with-Python/df_yelp_csv.csv', index=False)  
print(df_four.head(3))
print(df_yelp.head(3))

#use df_four_csv.csv, df_yelp_csv.csv for further analysis
# 5.Compare the quality of the Yelp and Foursquare API. 
# For your location, which API gives you the most complete information/better coverage? 
# *NOTE:* Your definition of 'coverage' is up to you. 
# It could be simple 'number of POIs in the area', but it could also be something more 
# specific like 'number of reviews per POI', or 'number of different attributes of each POI'.
# # Create DataFrames
# foursquare_df = pd.DataFrame(foursquare_results)
# yelp_df = pd.DataFrame(yelp_results)

# Analyze and compare the data
# ...
