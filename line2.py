import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df1 = pd.read_csv('dataset/WalmartSalesData.csv')

# Combine 'Date' and 'Time' columns into a single 'DateTime' column
df1['DateTime'] = pd.to_datetime(df1['Date'] + ' ' + df1['Time'], format='%d-%m-%Y %H:%M:%S')

# Extract day and month from 'DateTime'
df1['Day'] = df1['DateTime'].dt.day
df1['Month'] = df1['DateTime'].dt.month

# Filter data for the current and previous month
current_month = 3
previous_month = 2

df_current_month = df1[df1['Month'] == current_month]
df_previous_month = df1[df1['Month'] == previous_month]

# Aggregate Quantity

daily_quantity_current = df_current_month.groupby('Day')['Quantity'].sum().reset_index()
daily_quantity_previous = df_previous_month.groupby('Day')['Quantity'].sum().reset_index()

# Add a 'Month' column to distinguish the two dataframes
daily_quantity_current['Month'] = 'Current Month'
daily_quantity_previous['Month'] = 'Previous Month'

combined_quantity = pd.concat([daily_quantity_current, daily_quantity_previous])

fig = px.line(combined_quantity,
              x='Day',
              y='Quantity',
              color='Month',
              title='Quantities Sold',
              color_discrete_map={'Current Month': '#FF9A00', 'Previous Month': '#FFFF80'})

fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})


