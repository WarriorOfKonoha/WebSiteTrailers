# Django
from django.urls import path

# Owns
from .views_api import *

urlpatterns = [
    path('login/' , LoginView),
    path('register/' , RegisterView)
]