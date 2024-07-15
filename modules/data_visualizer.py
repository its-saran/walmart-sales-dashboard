import plotly.express as px


class Visualize:
    def __init__(self, config):
        self.config = config
        self.size = self.config['plotly']['chart_size']

    def chart_1(self, df_current_month, colors):
        color_map = {
            'Yangon': colors['first'],
            'Naypyitaw': colors['second'],
            'Mandalay': colors['third']
        }

        fig = px.bar(df_current_month, x='City', y='Revenue', title='Total Sales by City', color='City',
                     color_discrete_map=color_map)

        fig.update_traces(width=0.5)
        fig.update_layout(
            height=self.size['height'],
            width=self.size['width'],
            xaxis_fixedrange=True,
            yaxis_fixedrange=True,
            bargap=0.4,
            title={
                'text': 'Total Sales by City',
                'font': {'size': 14}
            },
            xaxis={'title': ''},
            legend={
                'x': 0.83,
                'y': 1.2,
                'xanchor': 'center',
                'yanchor': 'top',
                'title': {'text': ''}
            }
        )
        fig.update_yaxes(range=[30000, 40000], dtick=2000)
        return fig

    def chart_2(self, df_current_month, colors):
        color_map = {
            'Mandalay': colors['third'],
            'Naypyitaw': colors['second'],
            'Yangon': colors['first']
        }

        fig = px.scatter(df_current_month, x='Day', y='Quantity', size='Revenue', color='City',
                         hover_name='City', size_max=17,
                         title='Quantity Sold by city',
                         color_discrete_map=color_map
                         )

        fig.update_layout(
            height=self.size['height'],
            width=self.size['width'],
            xaxis_fixedrange=True,
            yaxis_fixedrange=True,
            legend={
                'x': 0.95,
                'y': 1.2,
                'xanchor': 'right',
                'yanchor': 'top',
                'title': {'text': ''}
            },
            title={
                'text': 'Quantity Sold by city',
                'font': {'size': 14}
            },
        )
        fig.update_yaxes(range=[0, 65])
        return fig

    def chart_3(self, combined_df, colors):
        color_map = {
            'Current Month': colors['first'],
            'Previous Month': colors['third']
        }

        fig = px.line(combined_df,
                      x='Day',
                      y='Quantity',
                      color='Month',
                      title='Quantities Sold',
                      color_discrete_map=color_map)

        fig.update_layout(
            height=self.size['height'],
            width=self.size['width'],
            xaxis_fixedrange=True,
            yaxis_fixedrange=True,
            legend={
                'x': 0.99,
                'y': 1.1,
                'xanchor': 'right',
                'yanchor': 'top',
                'traceorder': 'normal',
                'font': {'size': 12, },
                'bgcolor': 'rgba(0,0,0,0)',
                'title': {'text': ''}
            },
            title={
                'text': 'Quantities Sold',
                'font': {'size': 14}
            },
        )

        y_tickvals = [-200, -150, -100, -50, 0, 50, 100, 150, 200, 250, 300, 350, 400]
        y_ticktext = ['', '', '', '', '', '50', '', '150', '', '250', '', '350', '']

        fig.update_yaxes(range=[-200, 400], tickvals=y_tickvals, ticktext=y_ticktext)
        return fig

    def chart_4(self, df_current_month, colors):
        color_map = {
            'Cash': colors['first'],
            'Credit card': colors['second'],
            'Ewallet': colors['third']
        }

        fig = px.bar(df_current_month, x='Product line', y='Revenue', color='Payment method',
                     color_discrete_map=color_map,
                     barmode='group', title='Total Sales by Product Line')
        fig.update_layout(
            height=self.size['height'],
            width=self.size['width'],
            xaxis_fixedrange=True,
            yaxis_fixedrange=True,
            yaxis={'range': [0, 18000]},
            legend={
                'x': 1,
                'y': 1.2,
                'xanchor': 'right',
                'yanchor': 'top',
                'title': {'text': ''}
            },
            title={
                'text': 'Total Sales by Product Line',
                'font': {'size': 14}
            },
        )
        return fig

    def chart_5(self, df_current_month, colors):
        color_map = {
            'Yangon': colors['first'],
            'Naypyitaw': colors['second'],
            'Mandalay': colors['third']
        }

        fig = px.bar(df_current_month, x='TimeOfDay', y='Rating', color='City', barmode='stack',
                     title='Average Rating per City', text='Rating',
                     color_discrete_map=color_map)

        fig.update_traces(texttemplate='%{text:.2f}', textposition='inside')
        fig.update_layout(
            height=self.size['height'],
            width=self.size['width'],
            xaxis={'title': 'Time of Day'},
            xaxis_fixedrange=True,
            yaxis_fixedrange=True,
            yaxis={'range': [0, 35]},
            bargap=0.4,
            legend={
                'x': 0.95,
                'y': 1.2,
                'xanchor': 'right',
                'yanchor': 'top',
                'title': {'text': ''}
            },
            title={
                'text': 'Average Rating per City',
                'font': {'size': 14}
            },
        )

        return fig

    def chart_6(self, df_current_month, colors):
        color_map = {
            'Member': colors['first'],
            'Normal': colors['third']
        }

        fig = px.line(
            df_current_month,
            x='Day',
            y='Visits',
            color='Customer type',
            title='Daily Visits by Customer Type',
            color_discrete_map=color_map
        )

        fig.update_layout(
            height=self.size['height'],
            width=self.size['width'],
            xaxis_fixedrange=True,
            yaxis_fixedrange=True,
            legend={
                'x': 0.99,
                'y': 1.1,
                'xanchor': 'right',
                'yanchor': 'top',
                'traceorder': 'normal',
                'font': {'size': 12},
                'bgcolor': 'rgba(0,0,0,0)',
                'title': {'text': ''}
            },
            title={
                'text': 'Daily Visits by Customer Type',
                'font': {'size': 14}
            },
        )

        y_tickvals = [-10, -5, 0, 5, 10, 15, 20, 25, 30]
        y_ticktext = ['', '', '', '5', '10', '15', '20', '25', '30']
        fig.update_yaxes(range=[-10, 30], tickvals=y_tickvals, ticktext=y_ticktext)
        return fig
