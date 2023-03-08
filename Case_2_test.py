#!/usr/bin/env python
# coding: utf-8

# In[83]:


#pip install streamlit
#import kaggle

#api = kaggle.api
#api.get_config_value("username")

#!kaggle datasets download -d camnugent/california-housing-prices
#!unzip california-housing-prices.zip


# In[ ]:





# In[84]:


import pandas as pd
df = pd.read_csv('housing.csv')


# In[ ]:





# In[90]:


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


#Column naam veranderen
df.rename(columns={'longitude': 'lon', 'latitude': 'lat'}, inplace=True)



#slider widget housing price
slider_house_value = st.slider('Buying price of a house, starting from: ', 0, 550000, (150000, 250000))

slider_house_value_minimum = slider_house_value[0]
slider_house_value_maximum = slider_house_value[1]


##st.write('Show all houses starting from $', slider_house_value_minimum)
##st.write('With a maximum of $', slider_house_value_maximum)

#slider widget amount of bedrooms
slider_bedrooms = st.slider('Minimum number of bedrooms: ', 0, 10, 0)
df['number_of_bedrooms_per_household'] = df.total_bedrooms / df.households





slider_house_value_minimum = slider_house_value[0]
slider_house_value_maximum = slider_house_value[1]




#slider_house_value interactive with shown map
df3 = df.loc[df["median_house_value"] >= slider_house_value_minimum ]
df4 = df3.loc[df["median_house_value"] <= slider_house_value_maximum ]

#slider_bedrooms interactive with shown map
df5 = df4.loc[df["number_of_bedrooms_per_household"] >= slider_bedrooms ]

st.map(df5)




# In[ ]:





# In[ ]:





# In[ ]:




