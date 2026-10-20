import streamlit as st
from src.ui.base_layout import button_layout

def button():

    button_layout()
    col1, col2 = st.columns(2, gap='small')
    
    with col1:
        if st.button("Teacher Login", width='stretch'):
            st.session_state['login_type'] = "teacher"
            st.rerun()

    with col2:
        if st.button("Student Login", width='stretch'):
            st.session_state['login_type'] = "student"
            st.rerun()