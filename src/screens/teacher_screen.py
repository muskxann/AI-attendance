import streamlit as st
from src.components.header import header_dashboard
from src.components.dialogue import create_subject, share_subject
from src.database.db import check_teacher_exists, create_teacher, teacher_login, get_all_subjects
from src.ui.base_layout import background_dashboard, dashboard_button, text_input_layout, style_layout, container_layout
from src.components.subject_card import subject_card

def teacher_screen():
    background_dashboard()
    dashboard_button()
    text_input_layout()
    style_layout()
    container_layout()

    if 'teacher_login' not in st.session_state:
        st.session_state['teacher_login'] = 'register'

    if st.session_state.get("teacher_data") is not None:
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
    background_dashboard()
    dashboard_button()
    text_input_layout()
    style_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
                
    with c1:
        header_dashboard()
    with c2:
        st.header(f"Welcome, {teacher_data['name']}")
        if st.button("logout", width='stretch', shortcut='control+backspace'):
            st.session_state['login_type']= None
            st.session_state.is_logged_in = False
            st.session_state.user_role = None
            st.session_state.teacher_data = None
            st.rerun()

    st.divider()

    if "current_teacher_tab" not in st.session_state:
        st.session_state.current_teacher_tab = 'take_attendance'

    tab1, tab2, tab3 = st.columns(3)

    with tab1:
        type1 = 'secondary' if st.session_state.current_teacher_tab == 'take_attendance' else 'tertiary'
        if st.button("Take attendance", width='stretch', type=type1):
            st.session_state.current_teacher_tab = 'take_attendance'
            st.rerun()
    with tab2:
        type2 = 'secondary' if st.session_state.current_teacher_tab == 'manage_subjects' else 'tertiary'
        if st.button("Manage subjects", width='stretch', type=type2):
            st.session_state.current_teacher_tab = 'manage_subjects'
            st.rerun()
    with tab3:
        type3 = 'secondary' if st.session_state.current_teacher_tab == 'attendance_records' else 'tertiary'
        if st.button("Attendance records", width='stretch', type=type3):
            st.session_state.current_teacher_tab = 'attendance_records'
            st.rerun()

    st.divider()

    if st.session_state.current_teacher_tab == 'take_attendance':
        take_attendance()
    if st.session_state.current_teacher_tab == 'manage_subjects':
        manage_subjects()
    if st.session_state.current_teacher_tab == 'attendance_records':
        attendance_records()



def take_attendance():
    st.header("Take AI Attendance")



def manage_subjects():
    container_layout()
    
    teacher_id = st.session_state.teacher_data.get('teacher_id')
    
    subject = get_all_subjects(teacher_id)

    col1, col2 = st.columns(2, gap='xlarge')
    with col1:
        st.header("Manage Subjects")
    with col2:
        if st.button("Create new subjects", width='stretch', type='secondary'):
            create_subject(teacher_id)
            
    with st.container(border=True, key='styled'):
        if not subject:
            st.info("There is no subject to show, create new subject")
        for sub in subject:
            stats = [
                ("Classes", sub['total_class']),
                ("Students", sub['total_students']),
            ]

            subject_card(
                code = sub['subject_code'],
                name = sub['subject_name'],
                section =  sub['section'],
                stats = stats,
                footer_clb = share_btn(sub)
            )


def share_btn(sub):
    if st.button(f"Share code:{sub['subject_name']}", key=f"share_{sub['subject_code']}", type='primary'):
        share_subject(sub['subject_name'], sub["subject_code"])
    st.space()

def attendance_records():
    st.header("Check Attendance Records")
    
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

    container_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
            
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", width='stretch', shortcut='control+backspace', type='secondary'):
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
            if st.button("Register", width='stretch', shortcut='control+enter', type='primary'):
                success, message = register_teacher(teacher_username, teacher_name, teacher_password, confirm_password)

                if success:
                    st.success(message)
                    import time
                    time.sleep(2)
                    st.session_state['teacher_login'] = 'login'
                    st.rerun()
                else:
                    st.error(message)
            
        with col2:
            if st.button("Already a member? Login Instead", width='stretch', type='secondary'):
                st.session_state['teacher_login']='login'
                st.rerun() 
            

def login_screen():

    container_layout()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
        
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", width='stretch', shortcut='control+backspace', type='secondary'):
            st.session_state['login_type']= None
            st.rerun()
    
    with st.container(border=True, key='styled') :  
        st.header("Login using Password")
        teacher_username = st.text_input(label="Username", placeholder="Enter your username...")
        teacher_password = st.text_input(label="Password", placeholder="Enter your password...", type='password')

        col1, col2 = st.columns(2, gap='xlarge')

        with col1:
            if st.button("Login", width='stretch', shortcut='control+enter', type='primary'):
                if login_teacher(teacher_username, teacher_password):
                    st.toast("Welcome back!")
                    import time
                    time.sleep(1)
                    st.rerun()

                else:
                    st.error("Invalid Username or Password")
        

        with col2:
            if st.button("New here? Register now", width='stretch', type='secondary'):
                st.session_state['teacher_login']='register'
                st.rerun()