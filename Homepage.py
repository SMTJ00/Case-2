#!/usr/bin/env python
# coding: utf-8

# In[74]:


#pip install streamlit
#import kaggle

#api = kaggle.api
#api.get_config_value("username")

#!kaggle datasets download -d camnugent/california-housing-prices
#!unzip california-housing-prices.zip


# In[75]:


import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
from PIL import Image


# In[76]:


import pandas as pd
df = pd.read_csv('housing.csv')


# In[77]:


#Points of LA
# Define two points
lAPoint1 = (34.344389,  -118.683239)
lAPoint2 = (33.700741, -118.143398)

# Calculate x and y boundaries of square/rectangle
x_min = min(lAPoint1[0], lAPoint2[0])
x_max = max(lAPoint1[0], lAPoint2[0])
y_min = min(lAPoint1[1], lAPoint2[1])
y_max = max(lAPoint1[1], lAPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_LA = points[points_in_square(points, square)]
dfLA = pd.DataFrame(points_within_square_LA)


dfLA["place1"]="LA"
df["place1"] = dfLA["place1"]


# In[78]:


#Points of San diego
# Define two points
sDPoint1 = (33.131831,  -116.894776)
sDPoint2 = (32.532950, -117.290284)

# Calculate x and y boundaries of square/rectangle
x_min = min(sDPoint1[0], sDPoint2[0])
x_max = max(sDPoint1[0], sDPoint2[0])
y_min = min(sDPoint1[1], sDPoint2[1])
y_max = max(sDPoint1[1], sDPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_SD = points[points_in_square(points, square)]
dfSD = pd.DataFrame(points_within_square_SD)

dfSD["place2"]="SD"
df["place2"] = dfSD["place2"]


# In[79]:


#Points of Santa Barbara
# Define two points
sBPoint1 = (34.465679,  -119.640681)
sBPoint2 = (34.391768, -119.887873)
 
# Calculate x and y boundaries of square/rectangle
x_min = min(sBPoint1[0], sBPoint2[0])
x_max = max(sBPoint1[0], sBPoint2[0])
y_min = min(sBPoint1[1], sBPoint2[1])
y_max = max(sBPoint1[1], sBPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_SB = points[points_in_square(points, square)]
dfSB = pd.DataFrame(points_within_square_SB)


dfSB["place3"]="SB"
df["place3"] = dfSB["place3"]


# In[67]:


#Points of San Francisco
# Define two points
sFPoint1 = (37.707405,  -122.511810)
sFPoint2 = (37.833819, -122.355006)

# Calculate x and y boundaries of square/rectangle
x_min = min(sFPoint1[0], sFPoint2[0])
x_max = max(sFPoint1[0], sFPoint2[0])
y_min = min(sFPoint1[1], sFPoint2[1])
y_max = max(sFPoint1[1], sFPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_SF = points[points_in_square(points, square)]
dfSF = pd.DataFrame(points_within_square_SF)


dfSF["place4"]="SF"
df["place4"] = dfSF["place4"]


# In[ ]:


#Points of Sacramento
# Define two points
SPoint1 = (38.435635,  -121.328991)
SPoint2 = (38.687984, -121.581677)

# Calculate x and y boundaries of square/rectangle
x_min = min(SPoint1[0], SPoint2[0])
x_max = max(SPoint1[0], SPoint2[0])
y_min = min(SPoint1[1], SPoint2[1])
y_max = max(SPoint1[1], SPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_S = points[points_in_square(points, square)]
dfS = pd.DataFrame(points_within_square_S)


dfS["place5"]="S"
df["place5"] = dfS["place5"]


# In[ ]:


#Points of Eureka
# Define two points
EPoint1 = (40.744716,  -124.207702)
EPoint2 = (40.821564, -124.086076)

# Calculate x and y boundaries of square/rectangle
x_min = min(EPoint1[0], EPoint2[0])
x_max = max(EPoint1[0], EPoint2[0])
y_min = min(EPoint1[1], EPoint2[1])
y_max = max(EPoint1[1], EPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_E = points[points_in_square(points, square)]
dfE = pd.DataFrame(points_within_square_E)

dfE["place6"]="E"
df["place6"] = dfE["place6"]


# In[ ]:


#Points of Redding
# Define two points
RPoint1 = (40.461108,  -122.271422)
RPoint2 = (40.681994, -122.471922)

# Calculate x and y boundaries of square/rectangle
x_min = min(RPoint1[0], RPoint2[0])
x_max = max(RPoint1[0], RPoint2[0])
y_min = min(RPoint1[1], RPoint2[1])
y_max = max(RPoint1[1], RPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_R = points[points_in_square(points, square)]
dfR = pd.DataFrame(points_within_square_R)

dfR["place7"]="R"
df["place7"] = dfR["place7"]


# In[ ]:


#Points of Fresno
# Define two points
FPoint1 = (36.921774,  -119.646822)
FPoint2 = (36.663947, -119.938777)

# Calculate x and y boundaries of square/rectangle
x_min = min(FPoint1[0], FPoint2[0])
x_max = max(FPoint1[0], FPoint2[0])
y_min = min(FPoint1[1], FPoint2[1])
y_max = max(FPoint1[1], FPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_F = points[points_in_square(points, square)]
dfF = pd.DataFrame(points_within_square_F)

dfF["place8"]="F"
df["place8"] = dfF["place8"]


# In[ ]:


#Points of El Centro
# Define two points
eCPoint1 = (32.821909,  -115.602880)
eCPoint2 = (32.752494, -115.515676)

# Calculate x and y boundaries of square/rectangle
x_min = min(eCPoint1[0], eCPoint2[0])
x_max = max(eCPoint1[0], eCPoint2[0])
y_min = min(eCPoint1[1], eCPoint2[1])
y_max = max(eCPoint1[1], eCPoint2[1])

# Define square/rectangle using boundaries
square = pd.DataFrame({'latitude': [x_min, x_min, x_max, x_max],
                       'longitude': [y_min, y_max, y_max, y_min]})

# Define list of coordinates
points = pd.DataFrame({'latitude': df['latitude'], 'longitude': df['longitude']})

# Define function to check if points are within square/rectangle
def points_in_square(points, square):
    x_min, x_max, y_min, y_max = square['latitude'].min(), square['latitude'].max(), square['longitude'].min(), square['longitude'].max()
    return (points['latitude'] >= x_min) & (points['latitude'] <= x_max) & (points['longitude'] >= y_min) & (points['longitude'] <= y_max)

# Filter points that fall within square/rectangle
points_within_square_EC = points[points_in_square(points, square)]
dfEC = pd.DataFrame(points_within_square_EC)

dfEC["place9"]="EC"
df["place9"] = dfEC["place9"]


# In[68]:





#titel van pagina
st.title('Welcome on: ')


#Funds logo
image = Image.open('Funda_foto.jpg')

col1, col2, col3 = st.columns([1,1,6])

with col1:
    st.write("")

with col2:
    st.write("")

with col3:
    st.image(image)

#Intro page
st.write('Start today with your search to an area where your wishes would have had the biggest changes to actually come true! (in 1990, because houses are not affordable anymore nowadays...).')
    
#Column naam veranderen
df.rename(columns={'longitude': 'lon', 'latitude': 'lat'}, inplace=True)

#checkbox which state
place = st.radio(
    "What part of california do you want to see?",
    ('Whole of California',
     'Los Angeles', 
     'San Diego',
     "Santa Barbara", 
     "San Francisco", 
     "Sacramento",
     "Eureka",
     "Redding",
     "Fresno",
     "El Centro"))

#slider widget housing price
slider_house_value = st.slider('Buying price of a house, starting from (in USD):', 0, 550000, (15000, 400000))

slider_house_value_minimum = slider_house_value[0]
slider_house_value_maximum = slider_house_value[1]


##st.write('Show all houses starting from $', slider_house_value_minimum)
##st.write('With a maximum of $', slider_house_value_maximum)

#slider widget amount of bedrooms
slider_bedrooms = st.slider('Minimum number of bedrooms: ', 0, 10, 0)
df['number_of_bedrooms_per_household'] = df.total_bedrooms / df.households

#slider widget median_income
#slider_median_income = st.slider('Use this slider if you want to specify what kind of region you would like to live in, based on your monthly income'
                               # , 0, 300, (1, 10))

#slider_median_income_minimum = slider_median_income[0]
#slider_median_income_maximum = slider_median_income[1]

#slider widget amount of rooms
slider_rooms = st.slider('Minimum number of rooms: ', 0, 10, 3)
df['number_of_rooms_per_household'] = df.total_rooms / df.households




#slider_house_value interactive with shown map
df3 = df.loc[df["median_house_value"] >= slider_house_value_minimum ]
df4 = df3.loc[df["median_house_value"] <= slider_house_value_maximum ]

#slider_bedrooms interactive with shown map
df5 = df4.loc[df["number_of_bedrooms_per_household"] >= slider_bedrooms ]

#slider_rooms interactive with shown map
df6 = df5.loc[df["number_of_rooms_per_household"] >= slider_rooms ]

#slider median_income interactive with shown map
#df... = df5...loc[df["median_income"] >= slider_median_income_minimum ]
#df... = df....loc[df["median_income"] <= slider_median_income_maximum ]

#map
if place == 'Whole of California':
    df7 = df6
if place == 'Los Angeles':
    df7 = df6.loc[df['place1'] == 'LA']
if place == 'San Diego':
    df7 = df6.loc[df['place2'] == 'SD']
if place == 'Santa Barbara':
    df7 = df6.loc[df['place3'] == 'SB']
if place == 'San Francisco':
    df7 = df6.loc[df['place4'] == 'SF']
if place == 'Sacramento':
    df7 = df6.loc[df['place5'] == 'S']
if place == 'Eureka':
    df7 = df6.loc[df['place6'] == 'E']
if place == 'Redding':
    df7 = df6.loc[df['place7'] == 'R']
if place == 'Fresno':
    df7 = df6.loc[df['place8'] == 'F']
if place == 'El Centro':
    df7 = df6.loc[df['place9'] == 'EC']
    
    


st.map(df7)




# In[ ]:





# In[69]:


print(df7)


# In[ ]:





# In[ ]:




