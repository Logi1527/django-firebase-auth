# Django Firebase Authentication Backend

A secure Django REST Framework (DRF) backend backend featuring custom middleware that intercept and verify Firebase ID tokens passed from a frontend application.

## 🚀 Features
* **Firebase Token Verification:** Custom authentication backend leveraging Google's `firebase-admin` SDK.
* **On-the-Fly User Sync:** Automatically checks for existing Django users or registers a new profile locally matching the verified Firebase credentials.
* **CORS Configured:** Setup ready for seamless communication with cross-origin frontend frameworks (React, Flutter, Vue, etc.).

---

## 📂 Project Structure
```text
django-firebase-auth/
│
├── .gitignore                      # Crucial: Protects secrets and database
├── manage.py                       # Django management script
├── db.sqlite3                      # Local database (ignored by Git)
├── firebase-service-account.json   # Google private key (ignored by Git)
│
├── auth_project/                   # Main project settings directory
│   ├── settings.py
│   └── urls.py
│
└── firebase_auth/                  # Authentication app directory
    ├── authentication.py           # Custom Firebase Security Guard logic
    ├── views.py
    └── urls.py# django-firebase-auth
    🛠️ Local Development Setup
Follow these steps to set up and run this project locally on your machine.

1. Prerequisites
Ensure you have Python 3.x and Git installed on your operating system.

2. Clone the Repository
Bash
git clone <your-repository-url>
cd django-firebase-auth
3. Create and Activate a Virtual Environment
Windows:

Bash
python -m venv venv
venv\Scripts\activate
Mac/Linux:

Bash
python3 -m venv venv
source venv/bin/activate
4. Install Dependencies
Make sure your virtual environment is active (venv), then run:

Bash
pip install django djangorestframework django-cors-headers firebase-admin
5. Setup Firebase Service Credentials
Go to your Firebase Console -> Project Settings -> Service Accounts.

Generate a new private key and download the .json file.

Place this file directly inside your root project directory.

Rename it exactly to: firebase-service-account.json.

⚠️ Security Warning: Never commit firebase-service-account.json or your db.sqlite3 file to GitHub. They are safely listed in .gitignore.

6. Run Database Migrations
Bash
python manage.py migrate
7. Fire Up the Server
Bash
python manage.py runserver
The application will boot up locally at http://127.0.0.1:8000/.

🔐 How the Authentication Works
When a protected API endpoint is targeted, the client must include a Firebase identity token in the request header:

Plaintext
Authorization: Bearer <YOUR_FIREBASE_ID_TOKEN>
The custom FirebaseAuthentication class in firebase_auth/authentication.py intercepts this header, extracts the raw token, verifies it against Google's servers, and hooks the payload natively into Django's request.user framework.


Once you save this file, remember to run `git add README.md`, `git commit -m "docs: add README instructions"`, and `git push origin main` to sync it to GitHub!