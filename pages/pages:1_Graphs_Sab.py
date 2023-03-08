#!/usr/bin/env python
# coding: utf-8

# In[178]:


#pip install --user kaggle


# In[179]:


#from kaggle.api.kaggle_api_extended import KaggleApi
#api = KaggleApi()
#api.authenticate()


# In[ ]:





# In[180]:


#!kaggle datasets download -d camnugent/california-housing-prices


# In[181]:


import pandas as pd
import numpy as np
from zipfile import ZipFile
import os
import streamlit as st
#import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go 


# In[182]:


#zf = ZipFile('california-housing-prices.zip')
#zf.extractall()
#zf.close()

with ZipFile("/Users/sabrinathoen/case_goed/california-housing-prices.zip", 'r') as zObject:
     zObject.extractall(
        path="/Users/sabrinathoen/case_goed")
df = pd.read_csv('housing.csv')
              


# In[183]:


st.set_page_config(page_title="Graphs", page_icon="📈")


# In[184]:


#df = pd.read_csv('housing.csv')


# In[185]:


#df.head()


# In[186]:


df.info()


# In[187]:


#df.shape


# In[188]:


#df.columns


# In[189]:


#Title
st.title("Case 2: California Housing Prices")

#Sidebar
#with st.sidebar:
    #st.header("This is the header")
    #st.subheader("This is the subheading")

#Columns


# In[190]:


#InputOcean = st.sidebar.selectbox("Select Ocean Proximity", ("<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"))


# In[191]:


InputGraph = st.sidebar.selectbox("Select Graph/ Ocean Proximity", ("<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"))


# In[192]:


GraphSelect = df[df["ocean_proximity"] == InputGraph]


# In[193]:


#st.dataframe(GraphSelect)


# In[194]:


#tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

#with tab1:
   # st.header("this is tab 1")
    
#with tab2:
    #st.header("this is tab 2")


# In[ ]:





# In[195]:


import plotly.io as pio

df = GraphSelect

pio.templates.default = "plotly"

fig = px.scatter(df,
        x="median_house_value",
        y="total_rooms",
        color= "ocean_proximity",
        size = "population",
        color_discrete_sequence=px.colors.qualitative.Alphabet, log_x=True, size_max=40)

st.header("Total Rooms & Housing Values in ocean proximity")
st.plotly_chart(fig, use_container_width=True)


# In[ ]:





# In[196]:


fig = px.scatter(df,
        x="population", y="households",
        color= "ocean_proximity",
        size = "population",
        color_discrete_sequence=px.colors.qualitative.Alphabet, log_x=False, size_max=50)

st.header("Population & Households to Ocean Proximity")
st.plotly_chart(fig, use_container_width=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




