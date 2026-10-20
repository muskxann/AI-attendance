import streamlit as st
from src.components.header import header_dashboard
from PIL import Image
import numpy as np
from src.ui.base_layout import background_dashboard, dashboard_button, text_input_layout

def student_screen():
    background_dashboard()
    dashboard_button()
    text_input_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
        
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", width='stretch', shortcut='control+backspace'):
            st.session_state['login_type']= None
            st.rerun()

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
    </style>

""", unsafe_allow_html=True)
    
    with st.container(border=True, key='styled') : 

        st.header("Login Using Face Id")

        photo_source = st.camera_input(label="Position your face at center")

    
    if photo_source:
        np.array(Image.open(photo_source))

            


