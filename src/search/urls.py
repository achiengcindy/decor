from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('results', views.results, name='search_results'),
]