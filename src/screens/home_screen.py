import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import home_button

def home_screen():
    home_button()

    st.markdown("""
        <style>
            .st-key-styled{
                background: #2b1e3d; 
                border-radius: 25px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
                width: 900px !important;
                height: 900px !important;
                padding: 40px !important;
            }
        </style>
    """, unsafe_allow_html=True)

    with st.container(border=False, key='styled'):
        header_home()
        
        col1, col2 = st.columns(2, gap='small')

        with col1:
            if st.button("Teacher Login", width='stretch', type="primary"):
                st.session_state['login_type'] = "teacher"
                st.rerun()

        with col2:
            if st.button("Student Login", width='stretch', type="primary"):
                st.session_state['login_type'] = "student"
                st.rerun()
            