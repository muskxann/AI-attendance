import streamlit as st
from src.database.db import add_subjects, enroll_student_to_subject, add_attendance
from src.ui.base_layout import dashboard_button, text_input_layout
from src.pipelines.voice_pipeline import process_bulk_audio
import segno
import io
import pandas as pd
from PIL import Image
from src.database.config import supabase
from datetime import datetime

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
    join_url = f"{app_domain}?join-code={subject_code}"
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



@st.dialog("Auto enroll")
def auto_enroll_dialog(join_code):
    student_id = st.session_state.student_data['student_id']
    res = supabase.table('subjects').select('subject_id', 'subject_name').eq('subject_id', join_code).execute()

    if not res.data:
        st.warning("Not a valid code")
        if st.button('Close'):
            st.query_params.clear()
            st.rerun()

    else:
        check = supabase.table('subject_students').select('*').eq('student_id', student_id).eq('subject_id', res.data[0]['subject_id']).execute()
        if check.data:
            st.warning("You are already enrolled in the class")
            if st.button('Close'):
                st.query_params.clear()
                st.rerun()
            return

        st.header(f"Would you like to join in {res.data[0]['subject_name']} class?")
        col1,col2 = st.columns(2)

        with col1:
            if st.button("Enroll now!", type='primary', width='stretch'):
                enroll_student_to_subject(student_id,res.data[0]['subject_id'])
                st.success('Successfully Enrolled')
                st.query_params.clear()
                import time
                time.sleep(1)
                st.rerun()

        with col2:
            if st.button("No thanks", type='primary', width='stretch'):
                st.query_params.clear()
                st.rerun()

        
@st.dialog("Add Photos")
def add_photos_dialog():
    st.write('Add or Capture photos for AI Attendance')

    if 'photo_tab' not in st.session_state :
        st.session_state.photo_tab = 'camera'

    t1,t2 = st.columns(2)

    with t1:
        type_camera = 'primary' if st.session_state.photo_tab == 'camera' else 'tertiary'
        if st.button('Camera', type=type_camera, width='stretch'):
            st.session_state.photo_tab = 'camera'

    with t2:
        type_upload = 'primary' if st.session_state.photo_tab == 'upload' else 'tertiary'
        if st.button('Upload Photo', type=type_upload, width='stretch'):
            st.session_state.photo_tab = 'upload'

    if st.session_state.photo_tab == 'camera':
        cam_photo = st.camera_input("Take Snapshot", key='dialog_cam')
        if cam_photo:
            st.session_state.attendance_images.append(Image.open(cam_photo))
            st.toast("Photo Captured")
            st.rerun()

    if st.session_state.photo_tab == 'upload':
        upload_photo = st.file_uploader("Choose image files", type=['jpg', 'jpeg', 'png'], accept_multiple_files=True)
        if upload_photo:
            for f in upload_photo:
                st.session_state.attendance_images.append(Image.open(f))
            st.toast("Photo Uploaded")
            st.rerun()

    st.divider()
    if  st.button("Done", type='primary'):
        st.rerun()

@st.dialog("Attendance Record")
def attendance_result_dialog(df, log):
    st.write("Please review attendance before confirming")
    st.dataframe(df, hide_index=True)
    col1,col2 = st.columns(2)
    with col1:
        if st.button("Confirm!", type='primary', width='stretch'):
            try:
                add_attendance(log)
                st.toast("Successfully logged attendance")
                st.session_state.attendance_images = []
                st.rerun()
            except Exception as e:
                st.error("Data inserting error")
            
    with col2:
        if st.button("Discard", type='tertiary', width='stretch'):
            st.session_state.attendance_images = []
            st.rerun()

@st.dialog("Voice Attendance")
def voice_attendance_dialog(subject_id):
    st.info("Record audio of students saying I am present then AI will recognise the students")
    audio = st.audio_input("Record Classroom Audio")
    if st.button("Analyze Audio"):
        with st.spinner("Processing Audio data"):
            res = supabase.table('subject_students').select('*, students(*)').eq('subject_id',subject_id).execute()
            enrolled_students = res.data
            if not enrolled_students:
                st.warning("No students are enrolled in this course")
                return
            candidates_dict = {
                s["students"]['student_id'] : s['students']['voice_embedding']
                for s in enrolled_students if s['students'].get('voice_embedding')
            }
            if not candidates_dict:
                st.warning("No enrolled students have voice profiles registered")
                return
            audio_bytes = audio.read()
            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_log = [],[]
            current_timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

            for node in enrolled_students:
                student = node['students']
                scores = detected_scores.get(student['student_id'], 0.0)
                is_present=bool(scores)
                results.append({
                    "Name":student['name'],
                    "ID":student['student_id'],
                    "Score":scores if is_present else "-",
                    "Status":"Present" if is_present else "Absent"
                })
                attendance_to_log.append({
                    'student_id':student['student_id'],
                    'subject_id':subject_id,
                    'timestamps':current_timestamp,
                    'is_present':bool(is_present)
                })
            st.session_state.voice_attendance_results = (pd.DataFrame(results), attendance_to_log)    

            if st.session_state.voice_attendance_results is not None:
                st.divider()
                st.write("Please review attendance before confirming")
                st.dataframe(pd.DataFrame(results), hide_index=True)
                col1,col2 = st.columns(2)
                with col1:
                    if st.button("Confirm!", type='primary', width='stretch'):
                        try:
                            add_attendance(attendance_to_log)
                            st.toast("Successfully logged attendance")
                            st.session_state.voice_attendance_results = None
                            st.rerun()
                        except Exception as e:
                            st.error("Data inserting error")
                        
                with col2:
                    if st.button("Discard", type='tertiary', width='stretch'):
                        st.session_state.voice_attendance_results = None
                        st.rerun()



