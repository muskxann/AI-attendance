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

    subjects.pop('subject_students', None)
    subjects.pop('attendance_logs', None)

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