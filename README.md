# AI Attendance System

### Smart Attendance Automation Using Face & Voice Recognition

An AI-powered attendance management system designed to simplify attendance tracking using facial recognition and voice-based interaction. Built with Python and Streamlit, the application aims to make attendance management more efficient, accessible, and reliable.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/AI-ML-8A2BE2?style=for-the-badge" alt="AI and ML"/>
  <img src="https://img.shields.io/badge/Database-Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase"/>
</p>

---

## Overview

Traditional attendance systems often rely on manual registers or time-consuming verification processes. These methods can be inefficient and may introduce errors in attendance records.

**AI Attendance** explores an intelligent alternative by integrating facial recognition and voice-based interaction into an attendance management application.

The project combines machine learning libraries, a Streamlit interface, and database integration to support a more streamlined attendance workflow.

## Features

* **Facial Recognition:** Uses face recognition technology to support identity verification.
* **Voice-Based Interaction:** Incorporates voice recognition into the attendance workflow.
* **Interactive Interface:** Provides a user interface built with Streamlit.
* **Student and Teacher Workflows:** Organizes the application around student and teacher screens.
* **Database Integration:** Uses Supabase for backend data management.
* **Data Processing:** Leverages Python libraries for handling and processing data.
* **Authentication Support:** Includes authentication-related dependencies such as bcrypt.

## Technology Stack

| Technology       | Purpose                                                |
| ---------------- | ------------------------------------------------------ |
| Python           | Core application logic                                 |
| Streamlit        | Interactive web interface                              |
| face_recognition | Facial recognition functionality                       |
| dlib             | Face processing and related computer vision operations |
| NumPy            | Numerical computations                                 |
| Pandas           | Data manipulation and processing                       |
| Scikit-learn     | Machine learning utilities                             |
| Supabase         | Backend and database integration                       |
| bcrypt           | Password hashing                                       |
| Pillow           | Image processing                                       |
| Segno            | QR code generation                                     |

## Project Structure

```text
AI-attendance/
│
├── src/
│   ├── screens/
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   │
│   ├── components/
│   └── ui/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: The structure above illustrates the main application files and known screen modules. Additional files and subdirectories may exist within `src/`.*

## Getting Started

Follow these steps to run the project locally.

### Prerequisites

Make sure you have the following installed:

* Python 3.10 or a compatible version
* Git
* pip
* A Supabase project with the required database configuration

> **Note:** The `dlib` dependency can require additional setup depending on your operating system and Python version.

### 1. Clone the Repository

```bash
git clone https://github.com/muskxann/AI-attendance.git
```

Navigate to the project directory:

```bash
cd AI-attendance
```

### 2. Create a Virtual Environment

Create an isolated Python environment to manage project dependencies.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If installing `dlib` or the facial recognition model package fails, check the relevant installation instructions for your operating system.

### 4. Configure the Database

The project uses Supabase for backend integration.

1. Create a Supabase project.
2. Configure the database tables and authentication-related settings required by the application.
3. Add your Supabase connection details using the configuration expected by the application.
4. Keep credentials and secret keys out of your source code and Git history.

Refer to the official [Supabase documentation](https://supabase.com/docs) for database configuration and connection instructions.

**Security:** Never commit database passwords, service-role keys, or other sensitive credentials to a public repository.

### 5. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Once the server starts, open the local URL displayed in your terminal. Streamlit typically uses:

```text
http://localhost:8501
```

## How It Works

The application is organized into separate screens for different user workflows.

### 1. Application Entry Point

`app.py` initializes the Streamlit session state and determines which screen should be displayed.

### 2. User Interface

The application includes separate screens for:

* Home and initial navigation
* Student-related operations
* Teacher-related operations

### 3. AI-Based Recognition

The project includes dependencies for facial recognition and image processing. These libraries can support face-based identity verification within the attendance workflow.

Voice-based interaction is also part of the project's intended functionality.

### 4. Data Management

Supabase provides the backend integration used to manage application data.

The exact attendance-recording and verification workflow depends on the implementation of the individual screens and supporting modules.

## Dependencies

The project uses the following major Python packages:

* `streamlit`
* `face_recognition_models`
* `dlib-bin`
* `numpy`
* `pandas`
* `scikit-learn`
* `supabase`
* `bcrypt`
* `segno`
* `pillow`

All dependencies are listed in [`requirements.txt`](requirements.txt).

## Future Improvements

Potential enhancements for the project include:

* **Real-Time Face Verification:** Improve the speed and reliability of facial recognition during attendance.
* **Voice Authentication:** Develop a more robust voice verification workflow.
* **Attendance Analytics:** Introduce visual reports and attendance summaries.
* **Automated Reporting:** Export attendance records to CSV or PDF.
* **Role-Based Access Control:** Strengthen permissions for students, teachers, and administrators.
* **Improved Security:** Implement secure credential handling and appropriate access controls.
* **Deployment:** Make the application accessible through a hosted web interface.
* **Testing:** Add automated tests for recognition, authentication, and attendance workflows.

## Privacy and Security

Facial and voice data can be sensitive biometric information. Any deployment of this application should consider:

* Obtaining appropriate consent before collecting biometric data.
* Protecting stored attendance records and credentials.
* Restricting access to authorized users.
* Avoiding unnecessary retention of biometric information.
* Providing an appropriate process for correcting inaccurate attendance records.

## Contributing

Contributions, suggestions, and bug reports are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Test your implementation.
5. Submit a pull request with a clear description of your changes.

## Author

**Muskan Mundra**

* GitHub: [@muskxann](https://github.com/muskxann)

## License

No license is currently specified in this README. Please add an appropriate license file if you intend to distribute the project for reuse.

---

<p align="center">
  <b>Making attendance smarter with AI.</b>
</p>
