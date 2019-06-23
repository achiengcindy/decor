from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'payment'

urlpatterns = [
    path('lipa/', views.payment_lipa, name='lipa'),
]