#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

housing = pd.read_csv('housing.csv')

df = housing
housing


# In[88]:


chart_data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=['median_house_value', 'housing_median_age'])

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)
st.line_chart(chart_data)


# In[89]:


fig = px.pie(df, values='population', names='ocean_proximity', color_discrete_sequence=px.colors.qualitative.Alphabet)
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[90]:


fig = px.box(df, x="ocean_proximity", y="housing_median_age", color_discrete_sequence=px.colors.qualitative.Alphabet)
fig.show()
st.plotly_chart(fig, use_container_width=True)

txt = st.text_area('Text to analyze', '''
    Deze boxplotten laten zien hoe de leeftijden van de bewoners pler blok in cali zijn verdeeld op basis van
    hoe dichtbij/verweg de bewoners zijn van de oceaan.
    ''')
st.write('Sentiment:')


# In[ ]:





# In[91]:



fig = px.scatter(df, x="median_house_value", y="housing_median_age",
	         color_discrete_sequence=px.colors.qualitative.Alphabet,
                log_x=True, size_max=60)
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[92]:


fig = px.scatter(df, x="median_income", y="median_house_value",
	         size="population", color="ocean_proximity", color_discrete_sequence=px.colors.qualitative.Alphabet,
                log_x=True, size_max=60)
fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[86]:


fig = go.Figure(data=[go.Surface(z=df.values)])

fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                  width=500, height=500,
                  margin=dict(l=65, r=50, b=65, t=90))

fig.show()
st.plotly_chart(fig, use_container_width=True)


# In[ ]:




