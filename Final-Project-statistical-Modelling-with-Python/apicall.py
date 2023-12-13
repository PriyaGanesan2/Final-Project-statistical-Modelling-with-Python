import requests
import pandas as pd
import json
from pandas import json_normalize
#function foursquare api call
def get_venues_fs(latitude, longitude, radius, api_key, categories):
    """
    Get venues from foursquare with a specified place type and coordinates.
    Args:
        latitude (float): latitude for query (must be combined with longitude)
        longitude (float): longitude for query (must be combined with latitude)
        api_key (str): foursquare API to use for query
        categories (str) : Foursquare-recognized place type. If not passed no place_type will be specified. Separate ids with commas
    
    Returns:
       json -- returning all values now. should i/ how can i send only few values 
    """
    url="https://api.foursquare.com/v3/places/search"
    #get loc details in teh correct format
    location = f"{latitude},{longitude}"
    # set the params for firing the api
    params = {
        "categories": categories,
        "radius": radius,
        "ll":location,
        "fields": "name,location,geocodes,tips,description,distance,rating,tel,hours,stats,features,categories"
        
    }   
    headers = {
    "accept": "application/json",
    "Authorization": api_key
    } 
    
    # Make the foursquare API request and return response
    response = requests.get(url, params=params,headers=headers)
    data = response.json()
    results = data.get('results', [])
    df = pd.DataFrame(results)
    #df = json_normalize(results) 

    #save the data into a jason file in local dir
    with open('foursquare.json','w') as json_file:
        json.dump(data,json_file)
     # return df_foursquare    
    return data
    
   
# Function Yelp API
def query_yelp(lat, lon,api_key):
    # Make a request to Yelp API
    # Adjust parameters as needed
    url = "https://api.yelp.com/v3/businesses/search"
    headers = {
        'Authorization': 'Bearer {}'.format(api_key)
    }
    params = {
        "latitude": lat,
        "longitude": lon,
        "categories": "libraries,vegetarian",# Adjust categories as needed
        "radius": 1000,
        
    }
    #make the yelp Api call and return yelp response
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    businesses = data.get('businesses', [])
    df = pd.DataFrame(businesses)
    #print(df)
    #save the data into a jason file in local dir
    with open('yelp.json','w') as json_file:
        json.dump(data,json_file)
    return data
