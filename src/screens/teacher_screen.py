import streamlit as st
from src.components.header import header_dashboard
from src.database.db import check_teacher_exists, create_teacher, teacher_login
from src.ui.base_layout import background_dashboard, dashboard_button, text_input_layout, style_layout

def teacher_screen():
    background_dashboard()
    dashboard_button()
    text_input_layout()
    style_layout()
    
    if 'teacher_login' not in st.session_state:
        st.session_state['teacher_login'] = 'register'

    if "teacher_data" in st.session_state:
            teacher_dashboard()
    else:
        match st.session_state['teacher_login']:
            case 'login':
                login_screen()
            case 'register':
                register_screen()
            case None:
                register_screen()
    

def teacher_dashboard():
    teacher_data = st.session_state.teacher_data
    st.header(f"Welcome, {teacher_data["name"]}")
    
def register_teacher(teacher_username, teacher_name, teacher_password, confirm_password):
    if not teacher_username or not teacher_name or not teacher_password or not confirm_password:
        return False, "All fields are required"
    if (teacher_password!=confirm_password):
        return False, "Password doesn't match"
    if check_teacher_exists(teacher_username):
        return False, "Username already exists"

    try:
        create_teacher(teacher_username, teacher_name, teacher_password)
        return True, "Sucessfully registered, login now"
    except:
        return False, "Unexpected Error"

def login_teacher(username, password):
    if not username or not password:
        return False

    teacher = teacher_login(username, password)

    if teacher:
        st.session_state.user_role = "teacher"
        st.session_state.teacher_data = teacher
        st.session_state.is_logged_in = True
        return True


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
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
            
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", width='stretch', shortcut='control+backspace'):
            st.session_state['login_type']= None
            st.rerun()

    with st.container(border=True, key='styled') :  
        st.header("Register your Teacher Profile")
        teacher_username = st.text_input(label="Username", placeholder="Enter your username...")
        teacher_name = st.text_input(label="Full Name", placeholder="Enter your full name...")
        teacher_password = st.text_input(label="Password", placeholder="Enter your password...", type='password')
        confirm_password = st.text_input(label="Confirm Password", placeholder="Confirm your password...", type='password')

        col1, col2 = st.columns(2, gap='xlarge')

        with col1:
            if st.button("Register", width='stretch', shortcut='enter'):
                success, message = register_teacher(teacher_username, teacher_name, teacher_password, confirm_password)

                if success:
                    st.success(message)
                    import time
                    time.sleep(2)
                    st.session_state['teacher_login'] = 'login'
                    st.rerun
                else:
                    st.error(message)
            
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
    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
        
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", width='stretch', shortcut='control+backspace'):
            st.session_state['login_type']= None
            st.rerun()
    
    with st.container(border=True, key='styled') :  
        st.header("Login using Password")
        teacher_username = st.text_input(label="Username", placeholder="Enter your username...")
        teacher_password = st.text_input(label="Password", placeholder="Enter your password...", type='password')

        col1, col2 = st.columns(2, gap='xlarge')

        with col1:
            if st.button("Login", width='stretch', shortcut='enter'):
                if login_teacher(teacher_username, teacher_password):
                    st.toast("Welcome back!")
                    import time
                    time.sleep(1)
                    st.rerun()

                else:
                    st.error("Invalid Username or Password")
        

        with col2:
            if st.button("Register Instead", width='stretch'):
                st.session_state['teacher_login']='register'
                st.rerun()