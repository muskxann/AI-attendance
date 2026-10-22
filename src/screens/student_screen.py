import streamlit as st
from src.components.header import header_dashboard
from PIL import Image
import numpy as np
from src.ui.base_layout import background_dashboard, dashboard_button, text_input_layout, style_layout, container_layout
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_attendance_logs, get_enrolled_subjects, unenroll_student_to_subject
from src.components.dialogue import enroll_dialog
from src.components.subject_card import subject_card

def student_screen():
    background_dashboard()
    dashboard_button()
    text_input_layout()
    container_layout()

    show_registration = False
    
    if (
        st.session_state.get("is_logged_in", False)
        and st.session_state.get("user_role") == "student"
        and st.session_state.get("user_data") is not None
    ):
        student_dashboard()
        st.stop()


    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
        
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", width='stretch', shortcut='control+backspace', type='primary', icon=':material/home:'):
            st.session_state['login_type']= None
            st.rerun()

    
    
    with st.container(border=True, key='styled') : 

        st.header("Login Using Face Id")

        photo_source = st.camera_input(label="Position your face at center")

    
    if photo_source:
        img  = np.array(Image.open(photo_source))
        with st.spinner("AI is detecting..."):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces==0:
                st.warning("face not found!")
                show_registration=True
            elif num_faces>1:
                st.warning("multiple faces detected")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next(
                    (s for s in all_students
                        if str(s.get("student_id")) == str(student_id)
                    ),
                    None)
                
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student' 
                        st.session_state.user_data = student
                        st.toast("Welcome back")
                        import time
                        time.sleep(1)
                        st.rerun()
                else:
                    st.info("Face not recognised, you might be a new student!")
                    show_registration=True

    if show_registration:
        with st.container():
            st.header("Register here!")
            new_name = st.text_input(label="Name", placeholder="Enter your name")
            st.subheader("Optional : voice enrollment")
            st.info("Enroll your voice for voice only attendance")
            audio_input = None
            try:
                audio_input = st.audio_input("Record a short phrase like I am present")
            except Exception:
                st.error("Audio input error")
            if st.button("Create Account", type='primary'):
                if new_name:
                    with st.spinner("Creating Profile"):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()
                            voice_emb =None
                            if audio_input:
                                voice_emb = get_voice_embedding(audio_input.read())

                            response_data = create_student(new_name,face_embedding = face_emb,voice_embedding=voice_emb)
                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student' 
                                st.session_state.user_data = response_data[0]
                                st.toast("Profile Created")
                                import time
                                time.sleep(1)
                                st.rerun()
                            else:
                                st.error("Couldn't capture face for facial recognition")

                else:
                    st.error("Please enter your name")


def student_dashboard():
    background_dashboard()
    dashboard_button()
    text_input_layout()
    style_layout()
    container_layout()
    col1, col2 = st.columns(2, gap='xlarge')

    student = st.session_state.get("user_data")
    student_id = student['student_id']

    with col1:
        header_dashboard()
    with col2:
        st.header(f"Welcome, {student['name']}")
        if st.button("Logout", type='primary', width='stretch', icon=':material/logout:'):
            st.session_state.is_logged_in = False
            st.session_state.user_role = None
            st.session_state.user_data = None
            st.session_state['login_type'] = None
            st.rerun()

    st.divider()

    c1, c2 = st.columns(2, gap='xlarge')

    with c1:
        st.header("Your Enrolled Subjects")
    with c2:
        if st.button("Enroll new subject", type='primary', width='stretch'):
            enroll_dialog()

    st.space()

    with st.spinner("Loading your enrolled subjects"):
        subjects = get_enrolled_subjects(student_id)
        logs = get_attendance_logs(student_id)

    stats_map = {}

    for log in logs:
        sid = log['subject_id']

        if sid not in stats_map:
            stats_map[sid]={'total':0, 'attended':0}

        stats_map[sid]['total']+=1

        if log.get('is_present'):
            stats_map[sid]['attended']+=1

    def unenroll_btn(sid):
        if st.button("Unenroll from this course", width='stretch', type='secondary', key=sid):
            unenroll_student_to_subject(student_id,sid)
            st.toast("Unenrolled from this class")
            st.rerun()


    cols = st.columns(2)
    for i, subnode in enumerate(subjects):
        sub = subnode['subjects']
        sid = sub['subject_id']
        stats = stats_map.get(sid, {"total":0, "attended":0})
        with cols[i%2]:
            subject_card(
                name=sub['subject_name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('Total', stats['total']),
                    ('Attended', stats['attended'])
                ],
                footer_clb=unenroll_btn(sid)
            )

