import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('../dataset/WalmartSalesData.csv')

# Combine Date and Time into a single DateTime column
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M:%S')

# Extract Day and Month from DateTime
df['Day'] = df['DateTime'].dt.day
df['Month'] = df['DateTime'].dt.month

# Set current and previous months
current_month = 3
previous_month = 2

# Filter data for the current and previous months
df_current_month = df[df['Month'] == current_month]
df_previous_month = df[df['Month'] == previous_month]

# Group by Day and sum Revenue for current and previous months
daily_revenue_current = df_current_month.groupby('Day')['Revenue'].sum().reset_index()
daily_revenue_previous = df_previous_month.groupby('Day')['Revenue'].sum().reset_index()

# Label the data for the current and previous months
daily_revenue_current['Month'] = 'Current Month'
daily_revenue_previous['Month'] = 'Previous Month'

# Combine the data
combined_revenue = pd.concat([daily_revenue_current, daily_revenue_previous])

# Create the Plotly figure
fig = px.line(combined_revenue,
              x='Day',
              y='Revenue',
              color='Month',
              title='Daily Sales Comparison',
              color_discrete_map={'Current Month': '#FF9A00', 'Previous Month': '#FFFF80'})

# Update the layout to fix the axis range, position the legend, and format the y-axis
fig.update_layout(
    xaxis_fixedrange=True,
    yaxis_fixedrange=True,
    yaxis=dict(
        tickformat=",",
        title='Revenue',
        rangemode='tozero'
    ),
    legend=dict(
        x=1,
        y=1,
        xanchor='right',
        yanchor='top'
    )
)
fig.update_yaxes(range=[0,10000], dtick=3000)
# Display the Plotly figure in Streamlit
st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})