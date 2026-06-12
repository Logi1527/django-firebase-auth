from django.urls import path
from .views import RegisterView, ProfileView, MainAdminComponentView

urlpatterns = [
    # Public route for setting up accounts
    path('register/', RegisterView.as_view(), name='register'),
    
    # Protected route for standard profiles
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Guarded route for the main administration portal component
    path('admin-dashboard/', MainAdminComponentView.as_view(), name='admin-dashboard'),
]