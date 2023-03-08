#!/usr/bin/env python
# coding: utf-8

# In[8]:


#pip install streamlit
import kaggle

api = kaggle.api
api.get_config_value("username")

#!kaggle datasets download -d camnugent/california-housing-prices
#!unzip california-housing-prices.zip


# In[ ]:





# In[9]:


import pandas as pd
df = pd.read_csv('housing.csv')
df.head()


# In[13]:


import streamlit as st
import numpy as np
import pandas as pd
import pydeck as pdk

st.title('Dit is een titel')
st.dataframe(df)

df.rename(columns={'longitude': 'lon', 'latitude': 'lat'}, inplace=True)
chart_data = df[['lon', 'lat']]


age = st.slider('How old are you?', 0, 30, 4)
st.write("I'm ", age, 'years old')

df.rename(columns={'longitude': 'lon', 'latitude': 'lat'}, inplace=True)
chart_data = df[['lon', 'lat']]
chart_data2 = df[['population']]

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data2,
           get_position='[lon, lat]',
           radius=100,
           elevation_scale=4,
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))


# In[ ]:





# In[ ]:





# In[ ]:




