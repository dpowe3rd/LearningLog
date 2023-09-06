"""Defines URL patterns for users"""

from django.contrib.auth import login
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls
    path('', include('django.contrib.auth.urls')),
    # Login Page
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
    # Log out page
    path('logout/', views.logout_view, name='logout'),
    # Registration page
    path('registration/', views.register, name='register'),

]
