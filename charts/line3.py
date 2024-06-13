import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df1 = pd.read_csv('../dataset/WalmartSalesData.csv')

# Combine 'Date' and 'Time' columns into a single 'DateTime' column
df1['DateTime'] = pd.to_datetime(df1['Date'] + ' ' + df1['Time'], format='%d-%m-%Y %H:%M:%S')

# Extract day and month from 'DateTime'
df1['Day'] = df1['DateTime'].dt.day
df1['Month'] = df1['DateTime'].dt.month

current_month = 3

df_current_month = df1[df1['Month'] == current_month]

# Group by day and customer type, and then count transactions
df_grouped = df_current_month.groupby(['Day', 'Customer type']).size().reset_index(name='Total Transactions')

fig = px.line(
    df_grouped,
    x='Day',
    y='Total Transactions',
    color='Customer type',
    title='Total Transactions by Customer Type')

fig.update_layout(
    xaxis_fixedrange=True,
    yaxis_fixedrange=True,
    legend=dict(
        x=0.99,
        y=0.99,
        xanchor='right',
        yanchor='top',
        traceorder='normal',
        font=dict(
            size=12,
        ),
        bgcolor='rgba(0,0,0,0)',
    )
)

# Update y-axis range and tick interval, and customize tick labels
fig.update_yaxes(range=[-10, 30], dtick=10, tickvals=[0, 10, 20, 30])

st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})