"""Defines URL patterns for users"""

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [

    # Login Page
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # Log out page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Registration page
    path('registration/', views.register, name='register'),

]
