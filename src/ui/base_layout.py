import streamlit as st

def background_home():
    st.markdown("""
        <style>
            .stApp{
            background-image: linear-gradient(#f3f4f5, #ff9408); 
            }

        </style>
    """, unsafe_allow_html=True)

def background_dashboard():
    st.markdown("""
        <style>
            .stApp{
            background-image: linear-gradient(#941228, #fc8e09); 
            }

        </style>
    """, unsafe_allow_html=True)


def style_layout():
    st.markdown("""
        <style>

            @import url('https://fonts.googleapis.com/css2?family=Elsie:wght@400;900&family=Karla:ital,wght@0,200..800;1,200..800&display=swap');

            #MainMenu, header, footer{
                visibility: hidden;
            }

            .block-container{
                padding-top: 1.5 rem !important;
            }

            h2{
                font-family: "Elsie", serif !important;
                font-size: 3.5rem !important;
                line-height:1.1rem !important;
                margin-bottom:0rem !important;
                color: #fbae49 !important;
            }

            h1{
                font-family: "Elsie", serif !important;
                font-size: 3.5rem !important;
                line-height:1.1rem !important;
                margin-bottom:0rem !important;
            }

            h3,h4,p{
                font-family: "Karla", sans-serif !important;

            }


        </style>
    """, unsafe_allow_html=True)

def button_layout():
    st.markdown("""
        <style>
            button{
                height: 300px;
                width: 300px;
                border-radius: 5% !important;
                font-family: "Karla", serif !important;
                font-size: 3.5rem !important;
                background: rgba(255, 255, 255, 0.15) !important; 
                backdrop-filter: blur(10px) !important;
                border: 1px solid rgba(255, 255, 255, 0.25) !important;
                color: #ffffff !important;
                font-weight: 500 !important;
                cursor: pointer;
                letter-spacing: 0.5px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2) !important;
                transition: all 0.3s ease !important;

            }
            button:hover{
                border: 1px !important;
                border-color: white;
                background: rgba(255, 255, 255, 0.25) !important;
                border: 1px solid rgba(255, 255, 255, 0.4) !important;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
                transform: translateY(-2px);
            }

        </style>
    """
    ,unsafe_allow_html=True)