import firebase_admin
from firebase_admin import auth as firebase_auth
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.conf import settings
from .db import users_collection  

if not firebase_admin._apps:
    cred = firebase_admin.credentials.Certificate(settings.FIREBASE_SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return None  

        token = auth_header.split(' ')[1]

        try:
           
            decoded_token = firebase_auth.verify_id_token(token)
            email = decoded_token.get('email').lower().strip()

           
            mongo_user = users_collection.find_one({"email": email})
            
            if not mongo_user:
                raise exceptions.AuthenticationFailed('Firebase token valid, but no matching profile found in MongoDB.')

            
            mongo_user['_id'] = str(mongo_user['_id'])

           
            return (mongo_user, token)

        except Exception as e:
            raise exceptions.AuthenticationFailed(f'Firebase Authentication Failed: {str(e)}')