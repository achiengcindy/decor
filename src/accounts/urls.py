from django.urls import path , re_path 
from .views import register
urlpatterns = [
    path('register/', register, name='register'),
]