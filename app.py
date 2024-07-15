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

        st.set_page_config(
            layout=self.config['page']['layout'],
            page_title=self.config['page']['title'],
            page_icon=self.config['page']['icon'],
            initial_sidebar_state=self.config['page']['sidebar'],
            menu_items={
                'About': """
                            ## Walmart Sales Dashboard
                            
                            **GitHub**: https://github.com/AdieLaine/
                            
                            The AI Assistant named, Streamly, aims to provide the latest updates from Streamlit,
                            generate code snippets for Streamlit widgets,
                            and answer questions about Streamlit's latest features, issues, and more.
                            Streamly has been trained on the latest Streamlit updates and documentation.
                        """
            }
        )

    @staticmethod
    def place_chart(fig):
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})

    def plot_chart_1(self, df_current_month):
        df = self.transform.chart_1(df_current_month)
        fig = self.visualize.chart_1(df)
        self.place_chart(fig)

    def plot_chart_2(self, df_current_month):
        df = self.transform.chart_2(df_current_month)
        fig = self.visualize.chart_2(df)
        self.place_chart(fig)

    def plot_chart_3(self, df_current_month, df_previous_month):
        df = self.transform.chart_3(df_current_month, df_previous_month)
        fig = self.visualize.chart_3(df)
        self.place_chart(fig)

    def plot_chart_4(self, df_current_month):
        df = self.transform.chart_4(df_current_month)
        fig = self.visualize.chart_4(df)
        self.place_chart(fig)

    def plot_chart_5(self, df_current_month):
        df = self.transform.chart_5(df_current_month)
        fig = self.visualize.chart_5(df)
        self.place_chart(fig)

    def plot_chart_6(self, df_current_month):
        df = self.transform.chart_6(df_current_month)
        fig = self.visualize.chart_6(df)
        self.place_chart(fig)

    def show(self):
        st.sidebar.header('Select a month')
        option = st.sidebar.selectbox(' ', self.transform.get_month_names())

        st.subheader(f'{option}')
        df_current_month, df_previous_month = self.transform.filter_by_month(option)

        with st.container():
            col1, col2, col3 = st.columns(3)

            with col1:
                self.plot_chart_1(df_current_month)
            with col2:
                self.plot_chart_2(df_current_month)
            with col3:
                self.plot_chart_3(df_current_month, df_previous_month)

        with st.container():
            col4, col5, col6 = st.columns(3)

            with col4:
                self.plot_chart_4(df_current_month)
            with col5:
                self.plot_chart_5(df_current_month)
            with col6:
                self.plot_chart_6(df_current_month)


if __name__ == '__main__':
    config = load_config("config/config.json")
    dashboard = Dashboard(config)
    dashboard.show()
    Styles.inject(st, config)
