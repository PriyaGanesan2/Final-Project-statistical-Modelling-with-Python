# Final-Project-Statistical-Modelling-with-Python

## Project/Goals
## The objective of this project is to create a statistical model using Python. This involves fetching data from City Bikes, Foursquare, and Yelp APIs. A decision is made to choose data from either Yelp or Foursquare, depending on its suitability for a specific point of interest. For City Bikes, the bike station locations are focused on Toronto. The chosen data pertains to vegetarian restaurants and libraries around Toronto, gathered from Yelp. The collected information from City Bikes and Yelp is then combined.
## The subsequent Exploratory Data Analysis (EDA) phase encompasses visually exploring, cleaning, and preparing the data, in addition to conducting hypothesis testing. The ultimate goal of the project is to construct a statistical model that can analyze relationships and make predictions. The emphasis is particularly on understanding the impact of independent variables on the dependent variable.





## Process
## Part 1
###Explore API Structure:
####Investigated the structure of the CityBikes API to understand its components.
####Executed queries to the API and analyzed the format of the returned data.
###City Selection and Bike Station Retrieval:
####Selected a specific city covered by the CityBikes API to focus on.
####Retrieved information on all available bike stations within the chosen city using the API.
###Data Extraction for Each Bike Station:
####For each bike station identified, utilized the API to extract relevant details such as latitude, longitude, and the number of available bikes.
###JSON Parsing into Pandas DataFrame:
####Parsed the JSON objects obtained from the API into a structured Pandas dataframe for ease of analysis and manipulation.
###Notebook Completion - city_bikes.ipynb:
####Completed the Jupyter notebook named city_bikes.ipynb to showcase the step-by-step execution of the tasks mentioned above.
####Demonstrated the process of exploring the API, retrieving bike station data, extracting relevant information, and converting it into a Pandas dataframe.
The completed notebook city_bikes.ipynb demonstrates the above steps



## Part 2
## Connect to Foursquare API and yelp API to extract Data.

## For each of the bike stations in Part 1, query both APIs to retrieve information for the indian restaurants of Toronto location.

## Created a DataFrame for the Yelp results and Foursquare results. Created csv files.

## Compared the quality of the Yelp and Foursquare API data. Yelp API provided more complete data as mentioned in above steps.

## Yelp provides a greater coverage in terms of the number of poi fetched for vegeratian restaurants and libraries in Toronto compared to Foursquare.




## Results



Foursquare Vegetarina resturants - 140
Foursquare library - 135


Top 10 Vegetarian Friendly Restaurants 
Top 10 Libraries


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>category</th>
      <th>rating</th>
      <th>reviews</th>
      <th>formatted_address</th>
      <th>telephone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>9</th>
      <td>Fresh Kitchen + Juice Bar Front</td>
      <td>Vegan and Vegetarian Restaurant</td>
      <td>8.9</td>
      <td>19.0</td>
      <td>47 Front St E (Church Street), Toronto ON M5E 1B3</td>
      <td>(647) 693-7556</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Fresh on Bloor</td>
      <td>Vegan and Vegetarian Restaurant</td>
      <td>8.8</td>
      <td>380.0</td>
      <td>326 Bloor St W, Toronto ON M5S 1W5</td>
      <td>(416) 599-4442</td>
    </tr>
    <tr>
      <th>442</th>
      <td>Tori's Bakeshop</td>
      <td>Bakery</td>
      <td>8.7</td>
      <td>78.0</td>
      <td>2188 Queen St E (Balsam Ave), Toronto ON M4E 1E6</td>
      <td>(647) 350-6500</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Rosalinda</td>
      <td>Mexican</td>
      <td>8.7</td>
      <td>35.0</td>
      <td>133 Richmond St W, Toronto ON M5H 2L3</td>
      <td>(416) 907-0650</td>
    </tr>
    <tr>
      <th>49</th>
      <td>One Love Vegetarian</td>
      <td>Vegan and Vegetarian Restaurant</td>
      <td>8.4</td>
      <td>51.0</td>
      <td>854 Bathurst St (at London St), Toronto ON M5R...</td>
      <td>(416) 535-5683</td>
    </tr>
    <tr>
      <th>478</th>
      <td>Hello 123</td>
      <td>Vegan and Vegetarian Restaurant</td>
      <td>8.4</td>
      <td>36.0</td>
      <td>1122 Queen St W, Toronto ON M6J 1H9</td>
      <td>(416) 532-3555</td>
    </tr>
    <tr>
      <th>345</th>
      <td>YamChops</td>
      <td>Soup Spot</td>
      <td>8.4</td>
      <td>29.0</td>
      <td>705 College St, Toronto ON M6G 1C2</td>
      <td>(416) 645-0117</td>
    </tr>
    <tr>
      <th>403</th>
      <td>Fresh on Crawford</td>
      <td>Vegan and Vegetarian Restaurant</td>
      <td>8.3</td>
      <td>251.0</td>
      <td>894 Queen St W (at Crawford), Toronto ON M6J 1G3</td>
      <td>(416) 599-4442</td>
    </tr>
    <tr>
      <th>255</th>
      <td>Buddha's Vegetarian Foods</td>
      <td>Chinese</td>
      <td>8.3</td>
      <td>48.0</td>
      <td>666 Dundas St W (Bathurst St.), Toronto ON M5T...</td>
      <td>(416) 603-3811</td>
    </tr>
    <tr>
      <th>190</th>
      <td>Fresh on Spadina</td>
      <td>Vegan and Vegetarian Restaurant</td>
      <td>8.2</td>
      <td>419.0</td>
      <td>147 Spadina Ave (at Richmond St. W.), Toronto ...</td>
      <td>(416) 599-4442</td>
    </tr>
  </tbody>
</table>
</div>
## Challenges 
(discuss challenges you faced in the project)
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>category</th>
      <th>rating</th>
      <th>reviews</th>
      <th>formatted_address</th>
      <th>telephone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>59</th>
      <td>Toronto Public Library - Toronto Reference Lib...</td>
      <td>Library</td>
      <td>9.0</td>
      <td>378.0</td>
      <td>789 Yonge St (btwn Collier &amp; Asquith Ave), Tor...</td>
      <td>(416) 395-5577</td>
    </tr>
    <tr>
      <th>189</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>8.6</td>
      <td>42.0</td>
      <td>190 Fort York Blvd, Toronto ON M5V 0E7</td>
      <td>(416) 393-6240</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>8.3</td>
      <td>38.0</td>
      <td>239 College St (at Huron St.), Toronto ON M5T 1R5</td>
      <td>(416) 393-7746</td>
    </tr>
    <tr>
      <th>89</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>8.0</td>
      <td>11.0</td>
      <td>370 Broadview Ave (at Gerrard St E), Toronto O...</td>
      <td>(416) 393-7720</td>
    </tr>
    <tr>
      <th>325</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>7.9</td>
      <td>51.0</td>
      <td>1101 Bloor St W (at Gladstone), Toronto ON M6H...</td>
      <td>(416) 393-7674</td>
    </tr>
    <tr>
      <th>1597</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>7.8</td>
      <td>15.0</td>
      <td>3083 Yonge St (at Lawrence Ave.), Toronto ON M...</td>
      <td>(416) 393-7730</td>
    </tr>
    <tr>
      <th>146</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>7.6</td>
      <td>14.0</td>
      <td>701 Pape Ave (at Danforth Ave), Toronto ON M4K...</td>
      <td>(416) 393-7727</td>
    </tr>
    <tr>
      <th>3687</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>7.6</td>
      <td>8.0</td>
      <td>496 Birchmount Rd, Toronto ON M1K 1N8</td>
      <td>(416) 396-8890</td>
    </tr>
    <tr>
      <th>443</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>7.5</td>
      <td>15.0</td>
      <td>2161 Queen St E (at Lee St.), Toronto ON M4L 1J1</td>
      <td>(416) 393-7703</td>
    </tr>
    <tr>
      <th>183</th>
      <td>Toronto Public Library</td>
      <td>Library</td>
      <td>7.5</td>
      <td>12.0</td>
      <td>40 St Clair Ave E (at Yonge St.), Toronto ON M...</td>
      <td>(416) 393-7657</td>
    </tr>
  </tbody>
</table>
</div>

Yelp Vegetarian resturants- 723 entries
Yelp library  - 463
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>categories</th>
      <th>rating</th>
      <th>review</th>
      <th>address</th>
      <th>phone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>277</th>
      <td>Sunny Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>3</td>
      <td>40 Saint George Street, Room 6141, Toronto, ON...</td>
      <td></td>
    </tr>
    <tr>
      <th>1908</th>
      <td>KaSpace Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>9</td>
      <td>765 Queen Street E, Toronto, ON M4M 1H3, Canada</td>
      <td>+16476579600</td>
    </tr>
    <tr>
      <th>3350</th>
      <td>KaSpace Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>9</td>
      <td>1326 Gerrard Street  E, Toronto, ON M4L 1Z1, C...</td>
      <td>+16476579600</td>
    </tr>
    <tr>
      <th>1931</th>
      <td>Sunny Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>3</td>
      <td>789 Yonge Street, Toronto, ON M4W 2G8, Canada</td>
      <td></td>
    </tr>
    <tr>
      <th>1</th>
      <td>KaSpace Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>9</td>
      <td>1432 Gerrard Street East, Toronto, ON M4L 1Z6,...</td>
      <td>+16476579600</td>
    </tr>
    <tr>
      <th>127</th>
      <td>Sunny Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>3</td>
      <td>2 Bloor Street W, Toronto, ON M4W 3E2, Canada</td>
      <td></td>
    </tr>
    <tr>
      <th>98</th>
      <td>Sunny Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>3</td>
      <td>10 Spadina Road, Toronto, ON M5R 2S7, Canada</td>
      <td></td>
    </tr>
    <tr>
      <th>198</th>
      <td>KaSpace Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>9</td>
      <td>Jones 118 Jones Ave, Toronto, ON M4M 2Z9, Canada</td>
      <td>+16476579600</td>
    </tr>
    <tr>
      <th>3031</th>
      <td>Sunny Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>3</td>
      <td>55 Avenue Rd, Toronto, ON M5R 3L2, Canada</td>
      <td></td>
    </tr>
    <tr>
      <th>971</th>
      <td>Sunny Cafe</td>
      <td>Vegetarian</td>
      <td>5.0</td>
      <td>3</td>
      <td>322 Bloor Street W, Toronto, ON M5S 1W5, Canada</td>
      <td></td>
    </tr>
  </tbody>
</table>
</div>

<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>categories</th>
      <th>rating</th>
      <th>review</th>
      <th>address</th>
      <th>phone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1928</th>
      <td>John W. Graham Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>2</td>
      <td>789 Yonge Street, Toronto, ON M4W 2G8, Canada</td>
      <td>+14169785851</td>
    </tr>
    <tr>
      <th>375</th>
      <td>John M Kelly Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>1</td>
      <td>113 St. Joseph Street, Toronto, ON M5S 3C2, Ca...</td>
      <td></td>
    </tr>
    <tr>
      <th>276</th>
      <td>John W. Graham Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>2</td>
      <td>40 Saint George Street, Room 6141, Toronto, ON...</td>
      <td>+14169785851</td>
    </tr>
    <tr>
      <th>1889</th>
      <td>John W. Graham Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>2</td>
      <td>Toronto Reference Library, 789 Yonge St, 2nd f...</td>
      <td>+14169785851</td>
    </tr>
    <tr>
      <th>65</th>
      <td>John W. Graham Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>2</td>
      <td>10 King's College Road, Room 2402, Toronto, ON...</td>
      <td>+14169785851</td>
    </tr>
    <tr>
      <th>1243</th>
      <td>John M Kelly Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>1</td>
      <td>341 Yonge Street, Toronto, ON M5B 1S1, Canada</td>
      <td></td>
    </tr>
    <tr>
      <th>1249</th>
      <td>John W. Graham Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>2</td>
      <td>341 Yonge Street, Toronto, ON M5B 1S1, Canada</td>
      <td>+14169785851</td>
    </tr>
    <tr>
      <th>1700</th>
      <td>John W. Graham Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>2</td>
      <td>118-92 King Street E, Toronto, ON M5C 2V8, Canada</td>
      <td>+14169785851</td>
    </tr>
    <tr>
      <th>145</th>
      <td>John W. Graham Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>2</td>
      <td>15 King's College Cir, 2nd Fl, N Wing, Toronto...</td>
      <td>+14169785851</td>
    </tr>
    <tr>
      <th>3119</th>
      <td>John W. Graham Library</td>
      <td>Libraries</td>
      <td>5.0</td>
      <td>2</td>
      <td>56 Wellesley St W, Toronto, ON M5S 2S3, Canada</td>
      <td>+14169785851</td>
    </tr>
  </tbody>
</table>
</div>

## Part 3: Joining Data

1. Joined the data from Part 1 with the data from Part 2 to create a new dataframe. 
2. Use data visualization to explore the data. 
3. Create  SQLite database and store the data you've collected on the POIs.
Validate your data.

## Part 4: Building a Model

1. Build a regression model using Python’s `statsmodels` module that demonstrates a relationship between the number of bikes in a particular location and the characteristics of the POIs in that location.  
2. Interpret results. Expand on the model output, and derive insights from your model.
3. Stretch: can you think of a way to turn the above regression problem into a classification one? Without coding, can you sketch out how you would cast the problem specifically, and lay out your approaches?

Complete the **model_building.ipynb** notebook to demonstrate how you executed the tasks above.
## Future Goals
(what would you do if you had more time?)
