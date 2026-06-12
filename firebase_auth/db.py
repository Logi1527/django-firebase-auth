from pymongo import MongoClient
from django.conf import settings

# This establishes the connection using your settings setup
# Make sure MONGODB_URI is defined in your settings.py, or paste your string here directly
client = MongoClient(getattr(settings, "MONGODB_URI", "mongodb://localhost:27017/"))
db = client['robotics_club_db']

# Expose the users collection to your views and middleware
users_collection = db['users']