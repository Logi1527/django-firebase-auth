from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .authentication import FirebaseAuthentication

class VerifyUserView(APIView):
    # 1. Assign our custom Firebase security guard to this specific view
    authentication_classes = [FirebaseAuthentication]
    
    # 2. Lock the door: strictly require the user to be authenticated
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # 3. If the code reaches this point, the token was valid!
        # request.user was automatically populated by our authentication.py file
        return Response({
            "status": "success",
            "message": "Successfully authenticated with Firebase!",
            "django_username": request.user.username,
            "email": request.user.email
        })