from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from firebase_admin import auth
from django.contrib.auth.models import User

class FirebaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if not auth_header:
            return None
        
        try:
            token_type, token = auth_header.split(' ')
            if token_type.lower() != 'bearer':
                return None
        except ValueError:
            raise exceptions.AuthenticationFailed('Invalid token header format. Use "Bearer <token>".')

        try:
           
            decoded_token = auth.verify_id_token(token)
        except Exception as e:
            raise exceptions.AuthenticationFailed(f'Firebase Error: {str(e)}')


        uid = decoded_token.get('uid')
        email = decoded_token.get('email')

        user, created = User.objects.get_or_create(username=uid, defaults={'email': email})
        
        return (user, decoded_token)
