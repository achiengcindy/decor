from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>/', views.list_category, name='list_category'),
    path('<slug:slug>/', views.product_detail,name='product_detail'),
]

