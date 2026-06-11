from django.contrib import admin
from django.urls import path, include # Make sure 'include' is imported here!

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # ADD THIS LINE: This includes your app's local urls
    path('api/auth/', include('firebase_auth.urls')), 
]