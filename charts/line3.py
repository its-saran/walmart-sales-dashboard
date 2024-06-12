import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('../dataset/WalmartSalesData.csv')

# Combine 'Date' and 'Time' columns into a single 'DateTime' column
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M:%S')

# Extract day and month from 'DateTime'
df['Day'] = df['DateTime'].dt.day
df['Month'] = df['DateTime'].dt.month

current_month = 3

df_current_month = df[df['Month'] == current_month]

# Group by day and customer type, and then count transactions
df_grouped = df_current_month.groupby(['Day', 'Customer type']).size().reset_index(name='Total Transactions')

fig = px.line(
    df_grouped,
    x='Day',
    y='Total Transactions',
    color='Customer type',
    title='Total Transactions by Customer Type')

fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

