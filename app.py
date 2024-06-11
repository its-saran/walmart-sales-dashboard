import streamlit as st
import pandas as pd
import plotly.express as px

remove_branding = """
<style>
#MainMenu {visibility: hidden;}
.viewerBadge_container__r5tak {visibility: hidden;}
.viewerBadge_link__qRIco {visibility: hidden;}
</style>
"""

st.markdown(remove_branding, unsafe_allow_html=True)

df = pd.read_csv('dataset/WalmartSalesData.csv')

fig = px.bar(df, x='City', y='Revenue', title='Total Sales by City')
fig.update_traces(marker_color='#f17925')
fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

st.plotly_chart(fig, config={'displayModeBar': False})

