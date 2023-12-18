## Final-Project-Statistical-Modelling-with-Python

## 1.Project/Goals
### The objective of this project is to create a statistical model using Python. This involves fetching data from City Bikes, Foursquare, and Yelp APIs. A decision is made to choose data from either Yelp or Foursquare, depending on its suitability for a specific point of interest. For City Bikes, the bike station locations are in Toronto. The chosen point of interest data pertains to vegetarian restaurants and libraries around Toronto, gathered from Yelp. The collected information from City Bikes and Yelp is then combined.
#### The subsequent Exploratory Data Analysis (EDA) phase encompasses visually exploring, cleaning, and preparing the data, in addition to conducting hypothesis testing. The ultimate goal of the project is to construct a statistical model that can analyze relationships and make predictions. The emphasis is particularly on understanding the impact of independent variables on the dependent variable.

## 2.Process
## Part 1
### 1)Explore API Structure:
###    Investigated the structure of the CityBikes API to understand its components.
###    Executed queries to the API and analyzed the format of the returned data.
### 2)City Selection and Bike Station Retrieval:
###     Selected a specific city covered by the CityBikes API to focus on.
###     Retrieved information on all available bike stations within the chosen city using the API.
###     Data Extraction for Each Bike Station:
###     For each bike station identified, utilized the API to extract relevant details such as latitude, longitude, and the number of available bikes.
### 3)JSON Parsing into Pandas DataFrame:
###    Parsed the JSON objects obtained from the API into a structured Pandas dataframe for ease of analysis and manipulation.
###    copy the result in a csv file : [Final-Project-statistical-Modelling-with-Python/bike_info_csv.csv](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-
### 4)Link to the completed notebook demonstrates the above steps : https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/blob/3d62d049aa60aa69901805a1c706a45a50d34aab/Final-Project-statistical-Modelling-with-Python/notebooks/city_bikes.ipynb


## Part 2
### 1) Connect to Foursquare API and yelp API to extract Data.
### 2) For each of the bike stations in Toronto from Part 1, query both APIs to retrieve information for vegeratian restaurants and Libraries 
### 3) Created a DataFrame for Yelp results and Foursquare results and store this in csv files. 
####    YELP :https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/blob/3d62d049aa60aa69901805a1c706a45a50d34aab/Final-Project-statistical-Modelling-with-Python/yelp.csv
####    FOURSQUARE :https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/blob/3d62d049aa60aa69901805a1c706a45a50d34aab/Final-Project-statistical-Modelling-with-Python/foursquare.csv
### 4)Compared the quality of the Yelp and Foursquare API data:
####    1) Yelp provides a greater coverage in terms of the number of poi fetched for vegeratian restaurants and libraries in Toronto compared to Foursquar
####    2) Yelp Vegetarian resturants returned 723 entries Vs Foursquare Vegetarina resturants returned 140
####    3) Yelp library numbers - 463 Vs Foursquare library numbers - 135
### 4)Results


## To 10 Vegetarian Restaurants From Yelp
<div>

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
## Top 10 Libraries from Yelp
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
Foursquare data :
Foursquare Vegetarina resturants - 140
Foursquare library - 135


Top 10 Vegetarian Restaurants From Foursquare


<div>

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
## Top 10 Libraries from Foursquare
<div>

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





## link demonstrating Part 3 : [Final-Project-statistical-Modelling-with-Python/notebooks/yelp_foursquare_EDA.ipynb](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/blob/3d62d049aa60aa69901805a1c706a45a50d34aab/Final-Project-statistical-Modelling-with-Python/notebooks/yelp_foursquare_EDA.ipynb)

## Part 3: Joining Data

1. Joined the data from Part 1 with the data from Part 2 to create a new dataframe. 
2. EDA:
### 1.describe the data frames to undesrtand its structure, display top few records to understand the data, remove duplicates and then consider requires columns and create a new data frame for further analysis 
### 2.calculare and display the corelation between variables

<div>      
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>review</th>
      <th>rating</th>
      <th>distance</th>
      <th>free_bikes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>review</th>
      <td>1.000000</td>
      <td>0.237216</td>
      <td>0.061891</td>
      <td>-0.057693</td>
    </tr>
    <tr>
      <th>rating</th>
      <td>0.237216</td>
      <td>1.000000</td>
      <td>0.065995</td>
      <td>-0.072662</td>
    </tr>
    <tr>
      <th>distance</th>
      <td>0.061891</td>
      <td>0.065995</td>
      <td>1.000000</td>
      <td>-0.150368</td>
    </tr>
    <tr>
      <th>free_bikes</th>
      <td>-0.057693</td>
      <td>-0.072662</td>
      <td>-0.150368</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>

### 3. Display heat map to show the corelation: shows negative corelation between free bikes and review , free bikes and distance, free bikes and rating. The corelation shows a weak negative corelation.
![image](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/assets/110922792/7ff1616b-8cac-43cc-b20b-147611ac9700)

4.Use data visualization to explore the data.
   ![image](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/assets/110922792/6b8ab64d-47a8-489b-9fae-f4f252b1d9c5)
   ![image](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/assets/110922792/522eb434-8ba2-4d81-af45-27af31692144)
   ![image](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/assets/110922792/2a88d7f8-85de-4168-b864-5929bfcf4b03)
   ![image](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/assets/110922792/dfc1ecf0-51a8-4b2c-a03d-531f407ab385)
   ![image](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/assets/110922792/4bf5630f-b575-46bf-8778-11ba8bb4a99d)
   5.Explore the data.
        1)The correlation coefficient is -0.13251182646351062, close to 0 but negative - indicating a weak negative correlation. This means that as the 'distance' increases, there is a tendency for the 'free_bikes' to               decrease slightly, and as the 'distance' decreases, there is a tendency for the 'free_bikes' to increase slightly. However, the relationship is not very strong based on the absolute value of the correlation                coefficient.
          
      

6. Create  SQLite database and store the data you've collected on the POIs.
7. Validate your data before and after merge
8. Link to demonstrate pART 3: [Final-Project-statistical-Modelling-with-Python/notebooks/joining_data.ipynb](https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/blob/60bbaeff0219cfcc4c7c5d1eaea6ef7b7721e3b8/Final-Project-statistical-Modelling-with-Python/notebooks/joining_data.ipynb)

## Part 4: Building a Model

1. Build a regression model using Python’s `statsmodels` module that demonstrates a relationship between the number of bikes in a particular location and the characteristics of the POIs in that location.  
2. Interpret results. Expand on the model output, and derive insights from your model.
3. Model Results as below :
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:             free_bikes   R-squared:                       0.024
Model:                            OLS   Adj. R-squared:                  0.023
Method:                 Least Squares   F-statistic:                     45.04
Date:                Tue, 12 Dec 2023   Prob (F-statistic):           4.74e-20
Time:                        20:39:53   Log-Likelihood:                -13042.
No. Observations:                3677   AIC:                         2.609e+04
Df Residuals:                    3674   BIC:                         2.611e+04
Df Model:                           2                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         14.9342      0.708     21.079      0.000      13.545      16.323
distance      -0.0036      0.000     -7.865      0.000      -0.004      -0.003
rating        -0.8789      0.179     -4.897      0.000      -1.231      -0.527
==============================================================================
Omnibus:                      503.206   Durbin-Watson:                   0.219
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              747.675
Skew:                           0.997   Prob(JB):                    4.41e-163
Kurtosis:                       3.949   Cond. No.                     4.07e+03
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 4.07e+03. This might indicate that there are
strong multicollinearity or other numerical problems.

```
### Model Summary:
    
### 1) Dependent Variable:free_bikes
### 2) Coefficients:
###    *distance has a coef of -0.0036  and rating has a coef of -0.8789 
###    *distance: 'distance' is measured in meters, the negative coefficient suggests that as the distance from a location increases by one meter, the model predicts a small decrease in the number of free bikes. 
###    *rating:rating has a coef of -0.8789 indicatig negative relation.locations with higher ratings tend to have fewer free bikes.
### 3) Statistical Significance:
###    * P>|t| (p-value): All p values are 0 and less than 0.05. This indicates that we can reject null hypothesis and there is correlation between free bikes and distance and rating
### 4) Model Fit:
###    * R-squared: R-squared is 0.024 and Adj. R-squared is 0.023.Our model explains 2.3% of the variations in the data.R-squared is a measure of how well the chosen independent variables explain the changes in the dependent variable. A low R-squared, can be  seen in this model.    
### 5) The current model exhibits significant weaknesses in its ability to accurately predict bike availability.In this case, the model suggests that, on average, locations with higher ratings tend to have fewer free bikes, but it doesn't provide information about the underlying reasons for this relationship. Additional analysis and domain knowledge may be necessary to understand the implications of the observed relationships in this specific dataset.
### 6) Link for this activity: https://github.com/PriyaGanesan2/Final-Project-statistical-Modelling-with-Python/blob/60bbaeff0219cfcc4c7c5d1eaea6ef7b7721e3b8/Final-Project-statistical-Modelling-with-Python/notebooks/model_building.ipynb



## PART 5: Stretch: 
### can you think of a way to turn the above regression problem into a classification one? Without coding, can you sketch out how you would cast the problem specifically, and lay out your approaches?
####    1)Decide on a threshold value Create Categorical Labels:
####    2)Introduce a new categorical variable, say 'Availability Category,' where stations with free bikes above the threshold are labeled as "High" and others as "Low."
####    3)Update your dataset to include these new categories
####    4)Select a classification algorithm suitable for your dataset and problem. Common choices include logistic regression, decision trees, or random forests.
   


## Future Goals
### 1)Explore additional features that might better capture the relationships in the data. Additionally, interpreting the practical significance of coefficients and understanding the context of the problem a bit more in detail and come up with more a model that define the corelation between the variables and make meaningful statistical predications
### 2) Try the above stretch activity

