"""Defines URL patterns for users"""

from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    # Login Page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),


]