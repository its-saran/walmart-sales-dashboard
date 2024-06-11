import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('dataset/WalmartSalesData.csv')

fig = px.bar(df, x='City', y='Revenue', title='Total Sales by City')
fig.update_traces(marker_color='#f17925')
fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, config={'displayModeBar': False})

