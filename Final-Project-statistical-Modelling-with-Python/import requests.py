import requests
import pandas as pd

# 1. Explore the structure of the API and understand the data returned
# Example: CityBikes API endpoint for network information
#api_url = "https://api.citybik.es/v2/networks"

# Make a request to get information about available networks
#response = requests.get(api_url)
#data = response.json()

# Display the structure of the API response


# 2. Choose a city covered by the CityBikes API and retrieve all available bike stations in that city
# Let's assume we choose a city with a specific network ID (you need to check the actual available networks)
network_id = "bixi-toronto"

# Example: CityBikes API endpoint for stations in a specific network
stations_url = f"https://api.citybik.es/v2/networks/{network_id}"

# Make a request to get information about bike stations in the chosen city
stations_response = requests.get(stations_url)
stations_data = stations_response.json()

# Display the structure of the stations API response
#print(stations_data)

# 3. For each bike station, use the API to call the latitude, longitude, and number of bikes
# Parse the JSON object into a Pandas DataFrame
stations_list = stations_data.get("network", {}).get("stations", [])

# Create an empty DataFrame
columns = ["name", "latitude", "longitude", "bikes"]
df = pd.DataFrame(columns=columns)

# # Populate the DataFrame with station information
for station in stations_list:
    station_name = station.get("name")
    latitude = station.get("latitude")
    longitude = station.get("longitude")
    bikes = station.get("free_bikes")
    print(station_name) 
    df = df._append({"name": station_name, "latitude": latitude, "longitude": longitude, "bikes": bikes}, ignore_index=True)


