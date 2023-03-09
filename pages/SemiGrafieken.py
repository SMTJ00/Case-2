#!/usr/bin/env python
# coding: utf-8

# In[97]:


import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

housing = pd.read_csv('housing.csv')

df = housing


# In[ ]:





# In[101]:


fig = px.pie(df, values='population', names='ocean_proximity', color_discrete_sequence=px.colors.qualitative.Alphabet)
st.title('Piechart population VS ocean proximity')
st.plotly_chart(fig, use_container_width=True)


# In[107]:


st.title('Boxplots housing median age from each ocean distance')
fig = px.box(df, x="ocean_proximity", y="housing_median_age", color_discrete_sequence=px.colors.qualitative.Alphabet)
st.plotly_chart(fig, use_container_width=True)


# In[ ]:





# In[ ]:





# In[106]:


fig = px.scatter(df, x="median_income", y="median_house_value",
	         size="population", color="ocean_proximity", color_discrete_sequence=px.colors.qualitative.Alphabet,
                log_x=True, size_max=60)
st.title('Median house value VS median income for the location and population in california')
st.plotly_chart(fig, use_container_width=True)


# In[ ]:





# In[ ]:




