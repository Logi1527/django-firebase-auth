import os
from pathlib import Path
import firebase_admin
from firebase_admin import credentials
BASE_DIR = Path("c"\Users\DELL\Downloads\TRS\firebase-service-account.json).resolve().parent.pa

SECRET_KEY = 'your-temporary-secret-key'
DEBUG = True
ALLOWED_HOSTS = ['*']

# 1. Add applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'firebase_auth', # Your isolated auth app
]

# 2. Add CORS and Request Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Put this at the top
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'auth_project.urls'
WSGI_APPLICATION = 'auth_project.wsgi.application'

# 3. Allow your frontend local address to connect
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # Or whichever port your frontend uses
    "http://127.0.0.1:3000",
]

# 4. Initialize Firebase Admin SDK
# Place your downloaded Firebase Service Account JSON at the root of your project
FIREBASE_CRED_PATH = os.path.join(BASE_DIR, 'firebase-service-account.json')

if os.path.exists(FIREBASE_CRED_PATH):
    cred = credentials.Certificate(FIREBASE_CRED_PATH)
    firebase_admin.initialize_app(cred)
else:
    print("WARNING: firebase-service-account.json not found!")