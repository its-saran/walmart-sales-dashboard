import streamlit as st
import json
from modules import Transform, Visualize, Styles


def load_config(path):
    with open(path, 'r') as file:
        return json.load(file)


class Dashboard:
    def __init__(self, config):
        self.config = config
        self.transform = Transform(self.config)
        self.visualize = Visualize(self.config)
        self.color_schemes = config['app']['colors']
        self.colors = {}
        self.theme = {}

        st.set_page_config(
            layout=self.config['page']['layout'],
            page_title=self.config['page']['title'],
            page_icon=self.config['page']['icon'],
            initial_sidebar_state=self.config['page']['sidebar'],
            menu_items={
                'About': """
                            ## Walmart Sales Dashboard
                            
                            **GitHub**: https://github.com/its-saran/walmart-sales-dashboard
                            
                            An interactive web-based dashboard for visualizing Walmart sales data using Streamlit, Plotly, and Pandas.
                        """
            }
        )

    def plot_chart_1(self, df_current_month, colors):
        df = self.transform.chart_1(df_current_month)
        fig = self.visualize.chart_1(df, colors)
        self.place_chart(fig)

    def plot_chart_2(self, df_current_month, colors):
        df = self.transform.chart_2(df_current_month)
        fig = self.visualize.chart_2(df, colors)
        self.place_chart(fig)

    def plot_chart_3(self, df_current_month, df_previous_month, colors):
        df = self.transform.chart_3(df_current_month, df_previous_month)
        fig = self.visualize.chart_3(df, colors)
        self.place_chart(fig)

    def plot_chart_4(self, df_current_month, colors):
        df = self.transform.chart_4(df_current_month, colors)
        fig = self.visualize.chart_4(df, colors)
        self.place_chart(fig)

    def plot_chart_5(self, df_current_month, colors):
        df = self.transform.chart_5(df_current_month)
        fig = self.visualize.chart_5(df, colors)
        self.place_chart(fig)

    def plot_chart_6(self, df_current_month, colors):
        df = self.transform.chart_6(df_current_month)
        fig = self.visualize.chart_6(df, colors)
        self.place_chart(fig)

    @staticmethod
    def place_chart(fig):
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    def get_colors(self):
        return self.colors

    def show(self):
        with st.sidebar:
            st.markdown('# Walmart Sales Dashboard')
            st.markdown('### Select a month')
            option = st.sidebar.selectbox(' ', self.transform.get_month_names(), index=2, label_visibility="collapsed")

            st.markdown('### Select theme')
            color_option = st.sidebar.selectbox(' ', self.color_schemes.keys(), label_visibility="collapsed")

            self.colors = self.color_schemes[f'{color_option}']

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.subheader(f'{option}')
            with col2:
                pass

        df_current_month, df_previous_month = self.transform.filter_by_month(option)

        with st.container():
            col1, col2, col3 = st.columns(3)

            with col1:
                self.plot_chart_1(df_current_month, self.colors)
            with col2:
                self.plot_chart_2(df_current_month, self.colors)
            with col3:
                self.plot_chart_3(df_current_month, df_previous_month, self.colors)

        with st.container():
            col4, col5, col6 = st.columns(3)

            with col4:
                self.plot_chart_4(df_current_month, self.colors)
            with col5:
                self.plot_chart_5(df_current_month, self.colors)
            with col6:
                self.plot_chart_6(df_current_month, self.colors)



if __name__ == '__main__':
    config = load_config("config/config.json")
    dashboard = Dashboard(config)
    dashboard.show()
    colors = dashboard.get_colors()
    Styles.inject(st, colors)
