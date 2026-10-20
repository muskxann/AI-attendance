import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import background_dashboard, dashboard_button, text_input_layout

def teacher_screen():
    background_dashboard()
    dashboard_button()
    text_input_layout()
    
    if 'teacher_login' not in st.session_state:
        st.session_state['teacher_login'] = 'register'

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
        
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", width='stretch', shortcut='control+backspace'):
            st.session_state['login_type']= None
    
    match st.session_state['teacher_login']:
        case 'login':
            login_screen()
        case 'register':
            register_screen()
        case None:
            register_screen()

    


def register_screen(): 
    st.markdown("""
        <style>
            .st-key-styled{
                background: #e5cbd8; 
                border-radius: 25px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
            }
        </style>

""", unsafe_allow_html=True)
    with st.container(border=True, key='styled') :  
        st.header("Register your Teacher Profile")
        st.text_input(label="Username", placeholder="Enter your username...")
        st.text_input(label="Full Name", placeholder="Enter your full name...")
        st.text_input(label="Password", placeholder="Enter your password...", type='password')
        st.text_input(label="Confirm Password", placeholder="Confirm your password...", type='password')

        col1, col2 = st.columns(2, gap='xlarge')

        with col1:
            st.button("Register", width='stretch', shortcut='enter')
            

        with col2:
            if st.button("Login Instead", width='stretch'):
                st.session_state['teacher_login']='login'
                st.rerun() 
            



def login_screen():
    st.markdown("""
            <style>
                .st-key-styled{
                    background: #e5cbd8;
                    border-radius: 25px;
                    box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
                }
            </style>""", unsafe_allow_html=True)

    
    with st.container(border=True, key='styled') :  
        st.header("Login using Password")
        st.text_input(label="Username", placeholder="Enter your username...")
        st.text_input(label="Password", placeholder="Enter your password...", type='password')

        col1, col2 = st.columns(2, gap='xlarge')

        with col1:
            st.button("Login", width='stretch', shortcut='enter')
        

        with col2:
            if st.button("Register Instead", width='stretch'):
                st.session_state['teacher_login']='register'
                st.rerun()