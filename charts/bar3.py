import streamlit as st
import pandas as pd
import plotly.express as px


# Define a function to categorize time of day
def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'


# Load data
df = pd.read_csv('../dataset/WalmartSalesData.csv')


# Combine 'Date' and 'Time' columns into a single 'DateTime' column
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M:%S')
df['TimeOfDay'] = df['DateTime'].dt.hour.apply(categorize_time_of_day)


# Extract day and month from 'DateTime'
df['Day'] = df['DateTime'].dt.day
df['Month'] = df['DateTime'].dt.month


# Filter data for the current and previous month
current_month = 3
previous_month = 2


df_current_month = df[df['Month'] == current_month]

# Group data by 'TimeOfDay' and 'City' and calculate the average rating
avg_rating_per_city = df_current_month.groupby(['TimeOfDay', 'City'])['Rating'].mean().reset_index()

# Define a color map for each city
color_map = {
    'Yangon': '#fc3132',
    'Naypyitaw': '#fbc926',
    'Mandalay': '#2181fd'
}

# Create a stacked column chart using Plotly Express
fig = px.bar(avg_rating_per_city, x='TimeOfDay', y='Rating', color='City', barmode='stack',
             title='Average Rating per City by Time of Day', text='Rating',
             color_discrete_map=color_map)

# Update layout to display text inside bars
fig.update_traces(texttemplate='%{text:.2f}', textposition='inside')

fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
