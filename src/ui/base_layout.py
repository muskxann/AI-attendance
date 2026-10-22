import streamlit as st

def background_home():
    st.markdown("""
        <style>
            .stApp{
            background: #ceb7e1;
            }

        </style>
    """, unsafe_allow_html=True)

def background_dashboard():
    st.markdown("""
        <style>
            .stApp{
            background: #ceb7e1; 
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
                padding-top: 0rem;
            }

            h2{
                font-family: "Elsie", serif !important;
                font-size: 2rem !important;
                margin-bottom:0rem !important;
                color: #3c2857 !important;
            }

            h1{
                font-family: "Elsie", serif !important;
                font-size: 3.5rem !important;
                line-height:1.1rem !important;
                margin-bottom:0rem !important;
                color: #e5cbd8 !important;
            }

            h3,h4,p{
                font-family: "Karla", sans-serif !important;
                color: #3c2857 !important;
            }


        </style>
    """, unsafe_allow_html=True)

def home_button():
    st.markdown("""
        <style>
            button{
                height: 300px;
                width: 300px;
                border-radius: 5% !important;
                background: rgba(255, 255, 255, 0.15) !important; 
                backdrop-filter: blur(10px) !important;
                border: 1px solid rgba(255, 255, 255, 0.25) !important;
                cursor: pointer;
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

            [data-testid="stButton"] button p {
                font-family: 'Karla', sans-serif;
                font-size: 24px !important;    
                font-weight: 600 !important; 
                color: #ceb7e1 !important;  
            }

        </style>
    """
    ,unsafe_allow_html=True)

def dashboard_button():
    st.markdown("""
        <style>
            button[kind='primary']{
                border:0px !important;
                border-radius: 15px !important;
                font-family: "Karla", serif !important;
                background: #3c2857 !important; 
                cursor: pointer;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2) !important;
                transition: all 0.3s ease !important;
            }

            button[kind='primary']:hover{
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
                transform: translateY(-2px);
            }

            [data-testid="stButton"] button[kind='primary'] p {
                font-family: 'Karla', sans-serif;
                color: #e5cbd8 !important;
            }

            button[kind='secondary']{
                border-radius: 15px !important;
                font-family: "Karla", serif !important;
                background: rgba(255, 255, 255, 0.15) !important; 
                backdrop-filter: blur(10px) !important;
                border: 1px solid rgba(255, 255, 255, 0.25) !important;
                cursor: pointer;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2) !important;
                transition: all 0.3s ease !important;
            }

            button[kind='secondary']:hover{
                border: 1px !important;
                border-color: white;
                background: rgba(255, 255, 255, 0.25) !important;
                border: 1px solid rgba(255, 255, 255, 0.4) !important;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
                transform: translateY(-2px);
            }

            [data-testid="stButton"] button[kind='secondary'] p {
                font-family: 'Karla', sans-serif;
                color: #3c2857 !important;
            }

            button[kind='tertiary']{
                border:0px !important;
                border-radius: 15px !important;
                font-family: "Karla", serif !important;
                background: #e5cbd8 !important; 
                cursor: pointer;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.2) !important;
                transition: all 0.3s ease !important;
            }

            button[kind='tertiary']:hover{
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
                transform: translateY(-2px);
            }

            [data-testid="stButton"] button[kind='tertiary'] p {
                font-family: 'Karla', sans-serif;
                color: #3c2857 !important;
            }

        </style>
    """
    ,unsafe_allow_html=True)

def text_input_layout():
    st.markdown("""
        <style>
            [data-testid="stTextInputRootElement"] {
                background-color: #a38fbe !important;
                border-radius: 10px !important;
                border: transparent !important;
            }
            [data-testid="stTextInputRootElement"] input{
                color: white !important;
            }
        </style>
        """, unsafe_allow_html=True)

def container_layout():
    st.markdown("""
        <style>
            .st-key-styled{
                background: #e5cbd8; 
                border-radius: 25px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
            }
            div[data-testid="stCameraInput"] button {
                color: #3c2857 !important; 
            }
        </style>""", unsafe_allow_html=True)