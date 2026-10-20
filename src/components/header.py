import streamlit as st
from src.ui.base_layout import background_home, style_layout

def header_home():
    background_home()
    style_layout()
    st.markdown("""
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0&icon_names=school" />
        <div style="display:flex; flex-direction:column; justify-content:center; align-items:center; height:200px">
            <span class="material-symbols-outlined" style="transform: scale(4); color:#3c2857; margin-bottom:30px;">school</span>
            <h1>Smart Attendance</h1>
        </div>
    """, unsafe_allow_html=True)

def header_dashboard():
    style_layout()
    st.markdown("""
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0&icon_names=school" />
        <div style="display:flex; justify-content:center; align-items:center;">
            <span class="material-symbols-outlined" style="transform: scale(2); color: #3c2857; margin-right:20px;">school</span>
            <h2>Smart Attendance</h2>
        </div>
    """, unsafe_allow_html=True)