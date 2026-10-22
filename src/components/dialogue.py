import streamlit as st
from src.database.db import add_subjects, enroll_student_to_subject
from src.ui.base_layout import dashboard_button, text_input_layout
import segno
import io
from src.database.config import supabase

@st.dialog("Create New Subject")
def create_subject(teacher_id):
    dashboard_button()
    text_input_layout()
    subject_code = st.text_input("Code", placeholder="Enter Subject Code...")
    subject_name = st.text_input("Name", placeholder="Enter Subject Name...")
    section = st.text_input("Section", placeholder="Enter Section...")
    if st.button("Submit", type='primary'):
        if subject_code and subject_name and section:
            try:
                add_subjects(teacher_id,subject_code,subject_name,section)
                st.toast("Subject Created Successfully")
                st.rerun()
            except Exception as e:
                st.error("Unexpected error")
        else:
            st.warning("All fields are required")

@st.dialog("Share Class Link")
def share_subject(subject_name, subject_code):
    app_domain = "http://localhost:8502/"
    join_url = f"{app_domain}/?join-code={subject_code}"
    st.header("Scan to Join")
    qr = segno.make(join_url)
    out = io.BytesIO()
    qr.save(out, kind='png', scale=10, border=1)
    col1, col2 = st.columns(2)

    with col1:
        st.write("Copy Link")
        st.code(join_url, language='text')
        st.code(subject_code, language='text')
        st.info("Share this URL in Whatsapp or Email")

    with col2:
        st.write("Scan to join")
        st.image(out.getvalue(), caption="QR code to join the class")

@st.dialog("Enroll in a New Class")
def enroll_dialog():
    st.write("Join using subject code")
    join_code = st.text_input("subject code", placeholder='E.g. 101')
    if st.button("Enroll now", type='primary', width='stretch'):
        if not join_code:
            st.warning("Enter a valid code")
        else:
            res = supabase.table('subjects').select('subject_id', 'subject_code', 'subject_name').eq('subject_code', join_code).execute()
            if res.data:
                subject_data= res.data[0]
                student_id = st.session_state.user_data['student_id']
                check = supabase.table('subject_students').select('*').eq('student_id', student_id).eq('subject_id', subject_data['subject_id']).execute()
                if check.data:
                    st.warning("You are already enrolled")
                else:
                    enroll_student_to_subject(student_id,subject_data['subject_id'])
                    st.success('Successfully Enrolled')
                    import time
                    time.sleep(1)
                    st.rerun()

        
