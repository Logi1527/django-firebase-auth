from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .authentication import FirebaseAuthentication

class VerifyUserView(APIView):
    authentication_classes = [FirebaseAuthentication]
    
  
    permission_classes = [IsAuthenticated]

    def get(self, request):
       
        return Response({
            "status": "success",
            "message": "Successfully authenticated with Firebase!",
            "django_username": request.user.username,
            "email": request.user.email
        })
