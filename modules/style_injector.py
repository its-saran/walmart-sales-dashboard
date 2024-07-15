class Styles:
    @staticmethod
    def inject(st, config):

        css = f"""
            <style>
            
            #stDecoration {{
                visibility: hidden;
            }}

            .block-container.st-emotion-cache-1jicfl2.ea3mdgi5 {{
                padding-bottom: 0px;
                padding-top: 20px;
                padding-right: 25px;
                padding-left: 30px;
            }}

            #january, #march, #february {{
                padding-top: 0px;
                padding-left: 40px;
                font-size:22px;
                padding-bottom:13px;
                color: {config['app']['colors']['first']}
            }}
            
            ul[role="option"]:nth-of-type(1), 
            ul[role="option"]:nth-of-type(3),
            ul[role="option"]:nth-of-type(4){{
                display: None;
            }}
            
            ul div[data-testid="main-menu-divider"] {{
                display: None;
            }}
            
            .st-emotion-cache-17v3rtm.e1x90zqc9:nth-of-type(1)
             {{
                display: None;
            }}
            
            .st-emotion-cache-15yi2hn.e1x90zqc1 > div > p:nth-of-type(3)
             {{
                display: None;
            }}

            div[data-testid="stVerticalBlock"] {{
                gap: 0rem;
            }}

            .viewerBadge_container__r5tak.styles_viewerBadge__CvC9N {{
                z-index: -1;
            }}

            .viewerBadge_link__qRIco {{
                zindex: -1
            }}

            </style>
        """

        st.markdown(css, unsafe_allow_html=True)
