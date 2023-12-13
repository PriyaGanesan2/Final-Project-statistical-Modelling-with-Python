import requests
import pandas as pd
# assign netwrok id and url
# network_id="bixi-toronto"
def get_city_bikes_info(network_id):
    url=f"https://api.citybik.es/v2/networks/{network_id}"
    # call the API and fetch the response in JSON

    #get station details
    stations_response=requests.get(url)
    stations_data=stations_response.json()
    # for each bike station get the name, latitude, longitudee, number of ebikes and number of normal bikes
    stations_list=stations_data.get("network", {}).get("stations", [])

    #fetch the station name, latitude, longitude , number of available ebikes and normal bikes 
    #create a df and append the info into the df
    bike_info_df=pd.DataFrame(["name","latitude","longitude","ebikes","normalbikes"])
    for station in stations_list:
        station_name = station.get("name")
        free_bikes = station.get("free_bikes")
        latitude=station.get("latitude")
        longitude=station.get("longitude")
        ebike=station.get("extra",{}).get("ebikes")
        normalbike=station.get("extra",{}).get("normal_bikes")
        bike_info_df=bike_info_df._append({"name":station_name,"free_bikes":free_bikes,"latitude":latitude,"longitude":longitude},ignore_index=True)

    #save this df to a  csv
    bike_info_df=bike_info_df[bike_info_df.latitude.notna() & bike_info_df.longitude.notna()]
    bike_info_df.to_csv('../bike_info_csv.csv', index=False)
    return bike_info_df


