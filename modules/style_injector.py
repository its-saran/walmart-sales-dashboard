class Styles:
    @staticmethod



    def inject(st, colors):
        css = f"""
            <style>
            
            div[data-testid="stSidebarHeader"] {{
                padding-bottom: 0px;
            }}
            
            #stDecoration {{
                visibility: hidden;
            }}
            
            h3#january, 
            h3#february, 
            h3#march {{
                z-index: 9999;
                padding-top: 0px;
                padding-left: 40px;
                font-size: 22px;
                padding-bottom: 13px;
                color: {colors['first']}
            }}
            

            .block-container.st-emotion-cache-1jicfl2.ea3mdgi5 {{
                padding-bottom: 0px;
                padding-top: 20px;
                padding-right: 25px;
                padding-left: 30px;
            }}

            
            ul div[data-testid="main-menu-divider"] {{
                display: None;
            }}
            
            ul[role = "option"]:nth - of - type(1),
            ul[role = "option"]:nth - of - type(3),
            ul[role = "option"]:nth - of - type(4) {{
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
            
            div[data-testid="stSidebarContent"] div[data-testid="stMarkdownContainer"] h1 {{
                padding-top: 3px;
                margin-bottom: 30px;
                color: {colors['first']}
            }}
            
            div[data-testid="stSidebarUserContent"] .e1f1d6gn4 {{
                margin-bottom: 15px;
            }}
            
            </style>
        """

        st.markdown(css, unsafe_allow_html=True)


   # header
    # {{
    #     visibility: hidden;
    # }}

    # header[data - testid = "stHeader"] {{
    #     z - index: -999;
    # }}

    # header[data - testid = "stHeader"] {{
    #     background: {theme["background"]};
    # }}
    #
    # body
    # div[data - testid = "stApp"] {{
    #     background: {theme["background"]};
    # }}