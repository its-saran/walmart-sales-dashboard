import pandas as pd


class Transform:
    def __init__(self, config):
        self.config = config
        self.colors = self.config['app']['colors']
        self.df = pd.read_csv(self.config['data']['source'])
        self.df = self.add_datetime_features(self.df)

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
        df['MonthName'] = df['DateTime'].dt.month_name()
        df['TimeOfDay'] = df['DateTime'].dt.hour.apply(categorize_time_of_day)
        df = df.sort_values(by='DateTime')
        return df

    def filter_by_month(self, option):
        df = self.df
        current_month_df = df[df['MonthName'] == option].reset_index(drop=True)
        previous_month = (df[df['MonthName'] == option]['Month'].unique() - 1)[0]
        previous_month_df = None

        if previous_month:
            previous_month_df = df[df['Month'] == previous_month].reset_index(drop=True)
        return current_month_df, previous_month_df

    def get_month_names(self):
        return self.df['MonthName'].unique()

    def chart_1(self, df_current_month):
        return df_current_month

    def chart_2(self, df_current_month):
        grouped_data = df_current_month.groupby(['Day', 'City']).agg(
            {'Quantity': 'sum', 'Revenue': 'sum'}).reset_index()
        return grouped_data

    def chart_3(self, df_current_month, df_previous_month):
        daily_quantity_current = df_current_month.groupby('Day')['Quantity'].sum().reset_index()
        daily_quantity_current['Month'] = 'Current Month'
        combined_data = daily_quantity_current

        if df_previous_month is not None:
            daily_quantity_previous = df_previous_month.groupby('Day')['Quantity'].sum().reset_index()
            daily_quantity_previous['Month'] = 'Previous Month'

            combined_data = pd.concat([daily_quantity_current, daily_quantity_previous])

        return combined_data

    def chart_4(self, df_current_month):
        color_map = {
            'Cash': self.colors['first'],
            'Credit card': self.colors['second'],
            'Ewallet': self.colors['third']
        }
        grouped_data = df_current_month.groupby(['Product line', 'Payment method']).agg(
            {'Revenue': 'sum'}).reset_index()
        grouped_data['color'] = grouped_data['Payment method'].map(color_map)
        return grouped_data

    def chart_5(self, df_current_month):
        grouped_data = df_current_month.groupby(['TimeOfDay', 'City'])['Rating'].mean().reset_index()
        return grouped_data

    def chart_6(self, df_current_month):
        grouped_data = df_current_month.groupby(['Day', 'Customer type']).size().reset_index(name='Visits')
        return grouped_data



