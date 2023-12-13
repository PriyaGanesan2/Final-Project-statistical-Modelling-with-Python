import requests
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Step 1: Make API Requests
# CityBikes API
citybikes_url = "https://api.citybik.es/v2/networks/{network_id}"
citybikes_response = requests.get(citybikes_url)
citybikes_data = citybikes_response.json()

# Yelp API (Note: You need to provide your Yelp API key in the headers)
yelp_url = "https://api.yelp.com/v3/businesses/search"
headers = {'Authorization': 'Bearer YOUR_YELP_API_KEY'}
params = {'location': 'Your City', 'categories': 'Your Category', 'limit': 50}  # Adjust parameters
yelp_response = requests.get(yelp_url, headers=headers, params=params)
yelp_data = yelp_response.json()

# Step 2: Create DataFrames
citybikes_df = pd.DataFrame(citybikes_data['network']['stations'])
yelp_df = pd.DataFrame(yelp_data['businesses'])

# Step 3: Join DataFrames
# Assuming there is a common key, e.g., 'city'
merged_df = pd.merge(citybikes_df, yelp_df, left_on='city', right_on='location.city', how='inner')

# Step 4: Data Visualization
# Example: Scatter plot of the number of bikes vs. Yelp rating
plt.scatter(merged_df['free_bikes'], merged_df['rating'])
plt.xlabel('Number of Bikes')
plt.ylabel('Yelp Rating')
plt.title('Number of Bikes vs. Yelp Rating')
plt.show()

# Step 5: Create SQLite Database and Store Data
conn = sqlite3.connect('poi_data.db')  # Create or connect to the database
merged_df.to_sql('poi_data', conn, index=False, if_exists='replace')  # Write DataFrame to SQLite table
conn.commit()  # Commit changes
conn.close()  # Close the connection

