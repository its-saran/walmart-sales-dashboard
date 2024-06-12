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
df_previous_month = df[df['Month'] == previous_month]

daily_revenue_current = df_current_month.groupby('Day')['Revenue'].sum().reset_index()
daily_revenue_previous = df_previous_month.groupby('Day')['Revenue'].sum().reset_index()

daily_revenue_current['Month'] = 'Current Month'
daily_revenue_previous['Month'] = 'Previous Month'

combined_revenue = pd.concat([daily_revenue_current, daily_revenue_previous])

fig = px.line(combined_revenue,
              x='Day',
              y='Revenue',
              color='Month',
              title='Daily Sales',
              color_discrete_map={'Current Month': '#FF9A00', 'Previous Month': '#FFFF80'})

fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

