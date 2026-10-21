import streamlit as st
from src.components.header import header_dashboard
from PIL import Image
import numpy as np
from src.ui.base_layout import background_dashboard, dashboard_button, text_input_layout
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student

def student_screen():
    background_dashboard()
    dashboard_button()
    text_input_layout()
    show_registration = False

    if "student_data" in st.session_state:
        student_dashboard()
        st.rerun()

    c1, c2 = st.columns(2, vertical_alignment='center', gap='xlarge')
        
    with c1:
        header_dashboard()
    with c2:
        if st.button("Go back to home", width='stretch', shortcut='control+backspace'):
            st.session_state['login_type']= None
            st.rerun()

    st.markdown("""
    <style>
        .st-key-styled{
            background: #e5cbd8; 
            border-radius: 25px;
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.4) !important;
        }
        div[data-testid="stCameraInput"] button {
            color: #3c2857 !important; 
        }
    </style>

""", unsafe_allow_html=True)
    
    with st.container(border=True, key='styled') : 

        st.header("Login Using Face Id")

        photo_source = st.camera_input(label="Position your face at center")

    
    if photo_source:
        img  = np.array(Image.open(photo_source))
        with st.spinner("AI is detecting..."):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces==0:
                st.warning("face not found!")
            elif num_faces>1:
                st.warning("multiple faces detected")
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students
                    student = next((s for s in all_students if s['student_id']==student_id), None)
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
            if st.button("Create Account"):
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
    st.header(f"Welcome, {st.session_state.user_data['name']}")

