import streamlit as st
from src.database.db import add_subjects
from src.ui.base_layout import dashboard_button, text_input_layout

@st.dialog("Create New Subject")
def create_subject(teacher_id):
    dashboard_button()
    text_input_layout()
    st.header("Add a new subject")
    subject_code = st.text_input(placeholder="Enter Subject Code...")
    subject_name = st.text_input(placeholder="Enter Subject Name...")
    section = st.text_input(placeholder="Enter Section...")
    if st.button("Submit", type='primary'):
        if subject_code and subject_name and section:
            try:
                add_subjects(teacher_id,subject_code,subject_name,section)
                st.toast("Subject Created Successfully")
            except Exception as e:
                st.error("Unexpected error")
        else:
            st.warning("All fields are required")
