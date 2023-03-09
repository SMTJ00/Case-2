#!/usr/bin/env python
# coding: utf-8

# In[3]:


#pip install streamlit
#import kaggle

#api = kaggle.api
#api.get_config_value("username")

#!kaggle datasets download -d camnugent/california-housing-prices
#!unzip california-housing-prices.zip


# In[ ]:





# In[4]:


import pandas as pd
df = pd.read_csv('housing.csv')


# In[ ]:





# In[5]:


import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk
from PIL import Image


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

st.map(df6)




# In[6]:


print(df)


# In[ ]:





# In[ ]:




