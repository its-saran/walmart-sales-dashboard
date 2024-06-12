import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('../dataset/WalmartSalesData.csv')

df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M:%S')

df['Day'] = df['DateTime'].dt.day
df['Month'] = df['DateTime'].dt.month

current_month = 3
previous_month = 2

df_current_month = df[df['Month'] == current_month]

fig = px.bar(df_current_month, x='City', y='Revenue', title='Total Sales by City')
fig.update_traces(marker_color='#f17925')
fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
