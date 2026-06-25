"""Defines URL schemes for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Enable default authorization URL.
    path('', include('django.contrib.auth.urls')),    
]