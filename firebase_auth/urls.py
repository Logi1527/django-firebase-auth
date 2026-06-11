from django.urls import path
from .views import VerifyUserView

urlpatterns = [
    # This connects the '/verify/' URL to the View we built in Step 4
    path('verify/', VerifyUserView.as_view(), name='firebase-verify'),
]