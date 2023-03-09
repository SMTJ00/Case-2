#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
from zipfile import ZipFile
import os
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go 
import plotly.io as pio


# In[6]:


#zf = ZipFile('california-housing-prices.zip')
#zf.extractall()
#zf.close()

with ZipFile("/Users/sabrinathoen/case_goed/california-housing-prices.zip", 'r') as zObject:
     zObject.extractall(
        path="/Users/sabrinathoen/case_goed")
df = pd.read_csv('housing.csv')
              


# In[8]:


st.set_page_config(page_title="Distributions", page_icon="⚖️")


# In[9]:




pio.templates.default = "plotly"


fig = make_subplots(rows=3, cols=3, 
                   subplot_titles=["Housing Median Age", 
                                   "Total Rooms", 
                                   "Total Bedrooms", 
                                   "Population", 
                                   "Households", 
                                   "Median Income", 
                                   "Median House Value",
                                  "Longitude",
                                  "Latitude"])
fig.add_trace(
 go.Histogram(x=df['housing_median_age'], 
              marker=dict(color="darkcyan"), 
              name="Housing Median Age"),
    row=1, col=1)
    
fig.add_trace(
 go.Histogram(x=df['total_rooms'], 
              marker=dict(color="lightseagreen"), 
              name="Total rooms"),
            row=1, col=2)
    
fig.add_trace(
 go.Histogram(x=df['total_bedrooms'], 
              marker=dict(color="darkblue"),
              name='Total Bedrooms'),
            row=1, col=3)
    
fig.add_trace(
 go.Histogram(x=df['population'], 
              marker=dict(color="dodgerblue"), 
              name='Population'),
         row=2, col=1)
    
fig.add_trace(
 go.Histogram(x=df['households'], 
              marker=dict(color="aquamarine"), 
              name='Households'),
         row=2, col=2)
    
fig.add_trace(
 go.Histogram(x=df['median_income'], 
              marker=dict(color="mediumaquamarine"), 
              name='Median Income'),
             row=2, col=3)
    
fig.add_trace(
 go.Histogram(x=df['median_house_value'], 
              marker=dict(color="slateblue"), 
              name='Median House Value'),
         row=3, col=1)
    
fig.add_trace(
 go.Histogram(x=df['longitude'], 
              marker=dict(color="royalblue"), 
              name='Longitude'),
         row=3, col=2)
    
fig.add_trace(
 go.Histogram(x=df['latitude'], 
              marker=dict(color="darkolivegreen"), 
              name='Latitude'),
 row=3, col=3)


st.header("Distribution all values")
st.plotly_chart(fig, use_container_width=True)


# In[ ]:




