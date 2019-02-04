from django.urls import path
from .views import register, accounts_settings, accounts_edit,activate
urlpatterns = [
    path('register/', register, name='register'),
    path('settings/', accounts_settings, name='accounts_settings'),
    path('edit/', accounts_edit, name='accounts_edit'),
    path('activate/<slug:uidb64>/<slug:token>)/', activate, name='activate'),
]


