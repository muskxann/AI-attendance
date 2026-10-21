import streamlit as st
from src.database.db import add_subjects
from src.ui.base_layout import dashboard_button, text_input_layout
import segno
import io

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
