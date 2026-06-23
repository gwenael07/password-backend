from django.urls import path
from .views import generate_password_api

urlpatterns = [
    path('generate/', generate_password_api, name='generate_password'),
]