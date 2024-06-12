import streamlit as st
import pandas as pd
import plotly.express as px

class Dashboard:
    def __init__(self, path, current_month):
        self.df = pd.read_csv(path)
        self.current_month = current_month
        self.previous_month = current_month - 1
        self.df = self.add_datetime_features(self.df)
        self.df_current_month, self.df_previous_month = self.filter_by_month(self.df)

    def add_datetime_features(self, df):
        def categorize_time_of_day(hour):
            if 5 <= hour < 12:
                return 'Morning'
            elif 12 <= hour < 17:
                return 'Afternoon'
            elif 17 <= hour < 21:
                return 'Evening'
            else:
                return 'Night'

        df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %H:%M:%S')
        df['Day'] = df['DateTime'].dt.day
        df['Month'] = df['DateTime'].dt.month
        df['TimeOfDay'] = df['DateTime'].dt.hour.apply(categorize_time_of_day)
        return df

    def filter_by_month(self, df):
        df_current_month = df[df['Month'] == self.current_month]
        df_previous_month = df[df['Month'] == self.previous_month]
        return df_current_month, df_previous_month

    def plot_bar_chart_1(self, df_current_month):
        fig = px.bar(df_current_month, x='City', y='Revenue', title='Total Sales by City')
        fig.update_traces(marker_color='#f17925')
        fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)
        return fig

    def plot_bar_chart_2(self, df_current_month):
        grouped_data = df_current_month.groupby(['Product line', 'Payment method']).agg(
            {'Revenue': 'sum'}).reset_index()

        payment_colors = {
            'Cash': '#fc3132',
            'Credit card': '#fbc926',
            'Ewallet': '#2181fd'
        }

        # Map payment method colors
        grouped_data['color'] = grouped_data['Payment method'].map(payment_colors)

        fig = px.bar(grouped_data, x='Product line', y='Revenue', color='Payment method',
                     color_discrete_map=payment_colors,
                     barmode='group', title='Total Sales by Product Line')

        fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)
        return fig

    def plot_bar_chart_3(self, df_current_month):
        avg_rating_per_city = df_current_month.groupby(['TimeOfDay', 'City'])['Rating'].mean().reset_index()

        color_map = {
            'Yangon': '#fc3132',
            'Naypyitaw': '#fbc926',
            'Mandalay': '#2181fd'
        }

        fig = px.bar(avg_rating_per_city, x='TimeOfDay', y='Rating', color='City', barmode='stack',
                     title='Average Rating per City by Time of Day', text='Rating',
                     color_discrete_map=color_map)

        fig.update_traces(texttemplate='%{text:.2f}', textposition='inside')
        fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)

        return fig

    def plot_line_chart_1(self, df_current_month, df_previous_month):
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
        return fig

    def plot_line_chart_2(self, df_current_month, df_previous_month):
        daily_quantity_current = df_current_month.groupby('Day')['Quantity'].sum().reset_index()
        daily_quantity_previous = df_previous_month.groupby('Day')['Quantity'].sum().reset_index()

        daily_quantity_current['Month'] = 'Current Month'
        daily_quantity_previous['Month'] = 'Previous Month'

        combined_quantity = pd.concat([daily_quantity_current, daily_quantity_previous])

        # st.write(combined_quantity)

        fig = px.line(combined_quantity,
                      x='Day',
                      y='Quantity',
                      color='Month',
                      title='Quantities Sold',
                      color_discrete_map={'Current Month': '#2181fd', 'Previous Month': '#fc3132'})

        fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)
        return fig

    def plot_line_chart_3(self, df_current_month):
        grouped_data = df_current_month.groupby(['Day', 'Customer type']).size().reset_index(name='Total Transactions')

        fig = px.line(
            grouped_data,
            x='Day',
            y='Total Transactions',
            color='Customer type',
            title='Total Transactions by Customer Type')

        fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)
        return fig

    def plot_bubble_chart_1(self, df_current_month):
        daily_summary_current = df_current_month.groupby(['Day', 'City']).agg(
            {'Quantity': 'sum', 'Revenue': 'sum'}).reset_index()

        fig = px.scatter(daily_summary_current, x='Day', y='Quantity', size='Revenue', color='City',
                             hover_name='City', size_max=30,
                             title='Quantity Sold by city')

        fig.update_layout(xaxis_fixedrange=True, yaxis_fixedrange=True)
        return fig


    def show(self):
        st.title('Walmart Sales Dashboard')

        bar_chart_1 = self.plot_bar_chart_1(self.df_current_month)
        st.plotly_chart(bar_chart_1, use_container_width=True, config={'displayModeBar': False})


        bubble_chart_1 = self.plot_bubble_chart_1(self.df_current_month)
        st.plotly_chart(bubble_chart_1, use_container_width=True, config={'displayModeBar': False})


        bar_chart_2 = self.plot_bar_chart_2(self.df_current_month)
        st.plotly_chart(bar_chart_2, use_container_width=True, config={'displayModeBar': False})


        bar_chart_3 = self.plot_bar_chart_3(self.df_current_month)
        st.plotly_chart(bar_chart_3, use_container_width=True, config={'displayModeBar': False})


        line_chart_1 = self.plot_line_chart_1(self.df_current_month, self.df_previous_month)
        st.plotly_chart(line_chart_1, use_container_width=True, config={'displayModeBar': False})


        line_chart_2 = self.plot_line_chart_2(self.df_current_month, self.df_previous_month)
        st.plotly_chart(line_chart_2, use_container_width=True, config={'displayModeBar': False})


        line_chart_3 = self.plot_line_chart_3(self.df_current_month)
        st.plotly_chart(line_chart_3, use_container_width=True, config={'displayModeBar': False})



if __name__ == '__main__':
    dashboard = Dashboard('dataset/WalmartSalesData.csv', 3)
    dashboard.show()

