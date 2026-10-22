from src.database.config import supabase
import bcrypt

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def check_pass(pwd, hash_pwd):
    return bcrypt.checkpw(pwd.encode(), hash_pwd.encode())

def check_teacher_exists(username):
    response = supabase.table("teachers").select("username").eq("username", username).execute()

    return len(response.data)>0

def create_teacher(username, name, password):
    data = {
        "username": username,
        "name": name,
        "password": hash_pass(password)
    }
    response = supabase.table("teachers").insert(data).execute()

    return response.data


def create_student(name, face_embedding=None, voice_embedding=None):
    data = {
        "name": name,
        "face_embedding": face_embedding,
        "voice_embedding": voice_embedding
    }
    response = supabase.table("students").insert(data).execute()

    return response.data


def teacher_login(username, password):
    response = supabase.table("teachers").select("*").eq("username", username).execute()
    if response.data:
        teacher = response.data[0]
        if check_pass(password, teacher["password"]):
            return teacher
    return None

def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

def get_all_subjects(teacher_id):
    response = supabase.table("subjects").select("*", "subject_students(count)", "attendance_logs(timestamps)").eq("teacher_id",teacher_id).execute()
    subjects = response.data
    for subject in subjects:
        subject["total_students"] = subject.get("subject_students", [{}])[0].get('count', 0) if subject.get('subject_students') else 0
        attendance = subject.get('attendance_logs',[])
        unique_sessions = len(set(log['timestamp'] for log in attendance))
        subject['total_class'] = unique_sessions

    return subjects



def add_subjects(teacher_id, subject_code, subject_name, section):
    data = {
        "teacher_id":teacher_id,
        "subject_code":subject_code,
        "subject_name":subject_name,
        "section":section
    }
    response = supabase.table("subjects").insert(data).execute()
    return response.data

def enroll_student_to_subject(student_id, subject_id):
    data = {
        "student_id":student_id,
        "subject_id":subject_id
    }
    response = supabase.table('subject_students').insert(data).execute()
    return response.data

def unenroll_student_to_subject(student_id, subject_id):
    response = supabase.table('subject_students').delete().eq('student_id',student_id).eq('subject_id', subject_id).execute()
    return response.data

def get_attendance_logs(student_id):
    response = supabase.table('attendance_logs').select('*, subjects(*)').eq("student_id", student_id).execute()
    return response.data

def get_enrolled_subjects(student_id):
    response = supabase.table('subject_students').select('*, subjects(*)').eq('student_id', student_id).execute()
    return response.data

def add_attendance(log):
    res = supabase.table('attendance_logs').insert(log).execute()
    return res.data