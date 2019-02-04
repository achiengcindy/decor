from django.urls import path
from .views import order_details, order_create

app_name = 'orders'

urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('order_details/<int:order_id>/',order_details, name='order_details'),
]



