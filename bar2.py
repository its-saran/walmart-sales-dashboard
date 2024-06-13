import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('dataset/WalmartSalesData.csv')

# Combine 'Date' and 'Time' columns into a single 'DateTime' column
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M:%S')

# Extract day and month from 'DateTime'
df['Day'] = df['DateTime'].dt.day
df['Month'] = df['DateTime'].dt.month

# Filter data for the current and previous month
current_month = 3
previous_month = 2

df_current_month = df[df['Month'] == current_month]

# Group by product line and payment method, calculate total revenue
grouped_data = df_current_month.groupby(['Product line', 'Payment method']).agg({'Revenue': 'sum'}).reset_index()

# Define colors for payment methods
payment_colors = {
    'Cash': '#1f77b4',  # blue
    'Credit card': '#ff7f0e',  # orange
    'Ewallet': '#2ca02c'  # green
}

# Map payment method colors
grouped_data['color'] = grouped_data['Payment method'].map(payment_colors)

# Plot the bar chart
fig = px.bar(grouped_data, x='Product line', y='Revenue', color='Payment method', color_discrete_map=payment_colors,
             barmode='group', title='Total Sales by Product Line with Payment Method')

fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})