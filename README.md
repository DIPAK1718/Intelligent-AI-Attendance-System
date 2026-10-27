# 🤖 Intelligent AI Attendance System — Face & Voice Recognition

<p align="center">
  <strong>An AI-powered attendance management system that combines facial recognition, voice recognition, and role-based portals to streamline classroom attendance.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Application-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Computer%20Vision-Face%20Recognition-6C63FF?style=for-the-badge" alt="Computer Vision">
  <img src="https://img.shields.io/badge/Audio-Voice%20Recognition-0F9D8A?style=for-the-badge" alt="Voice Recognition">
  <img src="https://img.shields.io/badge/Status-Development-orange?style=for-the-badge" alt="Development Status">
</p>

---

## 📌 Overview

Traditional classroom attendance systems often rely on manual registers or time-consuming administrative processes.

The **Intelligent AI Attendance System** is designed to modernize attendance management by integrating face recognition, voice recognition, and dedicated student and teacher interfaces into a single application.

Built with Python and Streamlit, the project combines computer vision, audio processing, and backend integration to provide an interactive environment for attendance-related operations.

The application includes working student and teacher login flows, along with face and voice recognition functionality.

### 🎯 Project Objectives

* Explore AI-based identity recognition for attendance workflows.
* Integrate facial and voice recognition into a single application.
* Provide separate portals for students and teachers.
* Simplify attendance-related operations.
* Develop a modular application that can be maintained and extended.
* Apply AI/ML concepts to a practical educational use case.

---

## ✨ Features

### 👨‍🎓 Student Portal

* Student login.
* Student-facing application interface.
* Face registration and recognition workflow.
* Voice registration and recognition workflow.
* Access to student-related and attendance-related functionality.

### 👨‍🏫 Teacher Portal

* Teacher login.
* Teacher-facing application interface.
* Classroom and attendance management workflows.
* Access to student-related records and functionality.

### 🧠 AI-Powered Recognition

**1. Face Recognition**

The application incorporates facial recognition functionality to support identity-related operations.

The associated workflow can involve:

* Facial image input.
* Facial feature processing.
* Comparison with enrolled facial representations.
* Recognition results used by the application.

**2. Voice Recognition**

The application incorporates voice recognition functionality for voice-based identity-related operations.

The associated audio-processing workflow can involve:

* Voice input.
* Audio preprocessing.
* Voice representation extraction.
* Comparison with enrolled voice representations.

**3. Role-Based Navigation**

Students and teachers have separate login entry points, providing a foundation for role-specific application workflows.

**4. Backend Integration**

The project includes Supabase-related dependencies for backend and database functionality.

The exact database operations and access permissions depend on the configured application implementation.

---

## 🛠️ Technology Stack

| Technology              | Purpose                            |
| ----------------------- | ---------------------------------- |
| Python                  | Core application development       |
| Streamlit               | Interactive web application        |
| NumPy                   | Numerical computing                |
| Pandas                  | Data manipulation                  |
| scikit-learn            | Machine learning utilities         |
| dlib-bin                | Facial processing dependency       |
| face_recognition_models | Facial recognition model resources |
| librosa                 | Audio processing                   |
| Resemblyzer             | Voice embedding extraction         |
| Supabase                | Backend and database integration   |
| bcrypt                  | Password hashing utilities         |
| Pillow                  | Image processing                   |
| Segno                   | QR code generation                 |

The project also uses Python modules for interface components, database access, and processing pipelines.

*The table describes the project's dependency stack. Individual packages may be used by specific modules rather than throughout the entire application.*

---

## 🏗️ System Architecture

The application separates the user interface, role-specific screens, reusable components, database functionality, and processing pipelines.

```text
                 ┌─────────────────────────┐
                 │     Streamlit App       │
                 │        app.py           │
                 └────────────┬────────────┘
                              │
                 ┌────────────▼────────────┐
                 │       Home Screen       │
                 └────────────┬────────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
        ┌────────▼────────┐       ┌────────▼────────┐
        │ Student Screen  │       │ Teacher Screen  │
        └────────┬────────┘       └────────┬────────┘
                 │                         │
                 └────────────┬────────────┘
                              │
                 ┌────────────▼────────────┐
                 │   Application Logic     │
                 └────────────┬────────────┘
                              │
                ┌─────────────┴─────────────┐
                │                           │
       ┌────────▼────────┐        ┌─────────▼────────┐
       │ Face Recognition│        │ Voice Recognition│
       │    Pipeline     │        │     Pipeline     │
       └────────┬────────┘        └─────────┬────────┘
                │                           │
                └─────────────┬─────────────┘
                              │
                 ┌────────────▼────────────┐
                 │ Database / Backend      │
                 │ Supabase Integration    │
                 └─────────────────────────┘
```

*This diagram illustrates the conceptual architecture. The exact execution flow depends on the implemented modules.*

---

## 🔄 Application Workflow

### Step 1: Open the Application

The home screen presents separate entry points for students and teachers.

### Step 2: Log In

The user selects the appropriate portal and follows the corresponding login workflow.

### Step 3: Perform Recognition

Depending on the available workflow, the application processes facial or voice input using its recognition components.

### Step 4: Process the Result

The application uses the recognition result within the relevant workflow.

### Step 5: Access Attendance Functionality

Authorized users can access the attendance-related features available in their respective portals.

### Step 6: Manage Related Information

The application can interact with its configured backend for supported data operations.

> **Security note:** A successful face or voice match does not, by itself, prove that a person is physically present. Production deployments should consider liveness detection, replay protection, authorization, and biometric data privacy.

---

## 📂 Project Structure

The following structure reflects the main directories shown in the project workspace. Additional files may exist within the database and pipeline modules.

```text
Intelligent-AI-Attendance/
│
├── README.md
│
├── attendance-app/
│   ├── app.py
│   ├── requirements.txt
│   ├── .gitignore
│   │
│   ├── .streamlit/
│   │   └── secrets.toml
│   │
│   └── src/
│       ├── components/
│       │   ├── dialog_add_photo.py
│       │   ├── dialog_attendance_results.py
│       │   ├── dialog_auto_enroll.py
│       │   ├── dialog_create_subject.py
│       │   ├── dialog_enroll.py
│       │   ├── dialog_share_subject.py
│       │   ├── dialog_voice_attendance.py
│       │   ├── footer.py
│       │   ├── header.py
│       │   └── subject_card.py
│       │
│       ├── database/
│       │
│       ├── pipelines/
│       │
│       ├── screens/
│       │   ├── home_screen.py
│       │   ├── student_screen.py
│       │   └── teacher_screen.py
│       │
│       └── ui/
│           └── base_layout.py
│
└── .gitignore
```

**Important:** `.streamlit/secrets.toml` is shown to document the local configuration location. It must be excluded from Git if it contains credentials.

Virtual environments such as `.venv/` and `venv/` should also remain outside version control.

---

## ⚙️ Installation and Setup

### Prerequisites

* Python 3.11, subject to compatibility with the pinned dependencies.
* Git.
* Visual Studio Code or another Python development environment.
* Supabase credentials if required by your application configuration.

### 1. Clone the Repository

Replace `YOUR_USERNAME` and the repository name with your actual GitHub details.

```bash
git clone https://github.com/YOUR_USERNAME/Intelligent-AI-Attendance.git
```

Navigate to the application directory:

```bash
cd Intelligent-AI-Attendance/attendance-app
```

### 2. Create a Virtual Environment

On Windows PowerShell:

```powershell
py -3.11 -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Some computer vision and audio-processing packages may require compatible binary wheels or additional system dependencies.

If installation fails, verify your Python version and the dependency versions specified in `requirements.txt`.

### 4. Configure Application Secrets

Configure the environment variables or Streamlit secrets expected by your application.

For example, if the application expects these environment variable names:

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_key
```

Use the actual configuration mechanism implemented by the project. These names are examples and must match the code.

**Never commit real credentials to GitHub.** For deployment, configure secrets through the hosting provider's secure settings.

### 5. Run the Application

From the `attendance-app` directory:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, typically:

```text
http://localhost:8501
```

---

## 🧪 Testing Checklist

Before deployment, verify the following:

* [ ] Application starts without Python import errors.
* [ ] Home screen renders correctly.
* [ ] Student login works.
* [ ] Teacher login works.
* [ ] Face recognition workflow works with valid test inputs.
* [ ] Voice recognition workflow works with valid test inputs.
* [ ] Invalid or unrecognized identities are handled appropriately.
* [ ] Attendance-related operations behave correctly.
* [ ] Database access works with valid configuration.
* [ ] Missing or invalid credentials are handled safely.
* [ ] Secrets and biometric information are not exposed in the repository.

Recognition quality should be evaluated using an appropriate test dataset and clearly defined metrics. No accuracy or performance figure should be reported without measurement.

---

## 🔐 Security and Privacy

Facial and voice information can be sensitive biometric data. Secure handling is essential.

Recommended safeguards include:

* Obtain informed consent before collecting biometric information.
* Restrict access to enrolled facial and voice representations.
* Use secure password hashing and appropriate session management.
* Enforce authorization on protected backend operations.
* Keep API credentials and secrets outside source control.
* Avoid exposing biometric data in application logs.
* Define retention and deletion policies.
* Evaluate false acceptance and false rejection rates.
* Consider photographs, prerecorded audio, replay attacks, and synthetic media.
* Follow applicable privacy and data-protection requirements.

Recognition should not be treated as a guarantee of identity or physical presence without appropriate verification controls.

---

## 🚀 Deployment Considerations

Before deploying the application, verify that the hosting environment supports:

* The project's Python version and dependencies.
* Facial and audio-processing libraries.
* Required CPU, memory, and storage resources.
* Supabase connectivity and secure credential configuration.
* Any camera or microphone interaction required by the actual workflow.

A successful deployment of the home screen does not necessarily mean every recognition feature works in the hosted environment.

Test student login, teacher login, face recognition, voice recognition, and attendance operations after deployment.

---

## 🛣️ Future Enhancements

Potential improvements include:

* Facial and voice anti-spoofing mechanisms.
* Recognition evaluation and error analysis.
* Attendance analytics and reporting.
* Improved access controls and audit logging.
* Automated tests for authentication and recognition workflows.
* Better handling of low-quality images and noisy audio.
* Deployment optimization and dependency reduction.
* Improved accessibility and responsive UI behavior.
* Clear biometric consent and deletion workflows.

These are possible extensions and should not be interpreted as existing functionality unless implemented.

---

## 👨‍💻 Author

**Dipak Chaudhari**

B.Tech — Computer Science Engineering (Data Science)

Areas of interest:

* Artificial Intelligence and Machine Learning
* Computer Vision
* Deep Learning
* Generative AI

**GitHub:** [DIPAK1718](https://github.com/DIPAK1718)

**LinkedIn:** [dipak-chaudhari-ai](https://www.linkedin.com/in/dipak-chaudhari-ai/)

---

## 📄 License

A license has not yet been specified.

Choose an appropriate license before distributing the project. Without an applicable license, others do not automatically receive permission to reuse, modify, or redistribute the code.

---

<p align="center">
  <strong>Applying AI to build more efficient and responsible attendance workflows.</strong>
</p>
