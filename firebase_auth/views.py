from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .db import users_collection

# Import our brand new security layers
from firebase_auth.auth_backend import FirebaseAuthentication
from firebase_auth.permissions import IsClubAdmin

# ==========================================
# PUBLIC ENDPOINT: Registration
# ==========================================
class RegisterView(APIView):
    permission_classes = []  # Completely open to the public

    def post(self, request):
        data = request.data
        email = data.get('email', '').lower().strip()
        username = data.get('username', '')

        if not email or not username:
            return Response({"error": "Username and Email fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        # CRUD Duplicate Check
        if users_collection.find_one({"email": email}):
            return Response({"error": "This email is already registered."}, status=status.HTTP_400_BAD_REQUEST)

        # CRUD Create: Force default role as GUEST for safety
        new_user = {
            "username": username,
            "email": email,
            "role": "GUEST",  
            "skills": []
        }
        users_collection.insert_one(new_user)
        return Response({"message": "Profile created successfully in MongoDB."}, status=status.HTTP_201_CREATED)


# ==========================================
# PROTECTED MEMBER ENDPOINT: Profile CRUD
# ==========================================
class ProfileView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [] # Handled by the middleware token validation

    def get(self, request):
        # request.user is now the dict populated by our middleware
        user = request.user
        return Response({
            "username": user['username'],
            "email": user['email'],
            "role": user['role'],
            "skills": user.get('skills', [])
        }, status=status.HTTP_200_OK)


# ==========================================
# STRICT ADMIN ENDPOINT: Main Component Guard
# ==========================================
class MainAdminComponentView(APIView):
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsClubAdmin]  # Only grants access if role is 'ADMIN'

    def get(self, request):
        # This code is 100% safe. Regular users are blocked before hitting this line.
        return Response({
            "status": "success",
            "message": "Access granted. Welcome to the main Admin component dashboard data."
        }, status=status.HTTP_200_OK)