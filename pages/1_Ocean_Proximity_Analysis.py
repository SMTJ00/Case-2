#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install --user kaggle


# In[2]:


#from kaggle.api.kaggle_api_extended import KaggleApi
#api = KaggleApi()
#api.authenticate()


# In[ ]:





# In[3]:


#!kaggle datasets download -d camnugent/california-housing-prices


# In[4]:


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


# In[5]:


#zf = ZipFile('california-housing-prices.zip')
#zf.extractall()
#zf.close()

with ZipFile("/Users/sabrinathoen/case_goed/california-housing-prices.zip", 'r') as zObject:
     zObject.extractall(
        path="/Users/sabrinathoen/case_goed")
df = pd.read_csv('housing.csv')
              


# In[6]:


st.set_page_config(page_title="Ocean Proximity Analysis", page_icon="📈")


# In[7]:


#df = pd.read_csv('housing.csv')


# In[8]:


#df.head()


# In[9]:


df.info()


# In[10]:


#df.shape


# In[11]:


#df.columns


# In[12]:


#Title
st.title("Ocean Proximity Analysis")

#Text under title
st.write(
    """On this page illustrates a visual analysis of the variable Ocean Proximity. The first plot visualizes the relation between the total rooms per block, median house value and the proximity to the ocean. The second plot illustrates the relation between population and households per block and the ocean proximity. In the sidebar there's options to choose which data is visible. Enjoy!"""
)

#Sidebar
#with st.sidebar:
    #st.header("This is the header")
    #st.subheader("This is the subheading")

#Columns


# In[13]:


#InputOcean = st.sidebar.selectbox("Select Ocean Proximity", ("<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"))


# In[17]:


InputGraph = st.sidebar.selectbox("Select Ocean Proximity", ("<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"))


# In[18]:


GraphSelect = df[df["ocean_proximity"] == InputGraph]


# In[19]:


#st.dataframe(GraphSelect)


# In[20]:


#tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

#with tab1:
   # st.header("this is tab 1")
    
#with tab2:
    #st.header("this is tab 2")


# In[ ]:





# In[27]:


import plotly.io as pio

df = GraphSelect

pio.templates.default = "plotly"

fig = px.scatter(df,
        x="median_house_value",
        y="total_rooms",
                 title="Median house value per Total Rooms, per Ocean Proximity",
                 labels={"ocean_proximity": "Ocean Proximity",
                        "median_house_value": "Median Value of House",
                        "total_rooms": "Total Rooms per Block"},
        color= "ocean_proximity",
        size = "population", log_x=True, size_max=60)

st.header("Total Rooms & Housing Values in ocean proximity")
st.plotly_chart(fig, use_container_width=True, theme="streamlit")


# In[ ]:





# In[26]:


fig = px.scatter(df,
        x="population", y="households",
                 title="Population and Household, per Proximity to Ocean",
                     labels={"ocean_proximity": "Ocean Proximity",
                        "population": "Population per Block",
                        "households": "Households per Block"},
        color= "ocean_proximity",
        size = "population",
        color_discrete_sequence=px.colors.qualitative.Alphabet, log_x=False, size_max=60)

st.header("Population & Households to Ocean Proximity")
st.plotly_chart(fig, use_container_width=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




