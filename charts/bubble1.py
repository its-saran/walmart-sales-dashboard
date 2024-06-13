import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('../dataset/WalmartSalesData.csv')

df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M:%S')

df['Day'] = df['DateTime'].dt.day
df['Month'] = df['DateTime'].dt.month

current_month = 3
previous_month = 2

df_current_month = df[df['Month'] == current_month]

daily_summary_current = df_current_month.groupby(['Day', 'City']).agg({'Quantity': 'sum', 'Revenue': 'sum'}).reset_index()

# Display the grouped data
st.write(daily_summary_current)

fig = px.scatter(daily_summary_current, x='Day', y='Quantity', size='Revenue', color='City',
                 hover_name='City', size_max=60,
                 title='Quantity Sold by city')

fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})


