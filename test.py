import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Streamlit Bar Chart Example")

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 15, 25]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)


# # Create a Plotly Express bar chart
fig = px.bar(df, x='Category', y='Values', title='Bar Chart Example')


# Display the bar chart
st.plotly_chart(fig, use_container_width=True)

