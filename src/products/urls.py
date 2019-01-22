from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.list_category, name='product_clist_categoryategory'),
    # path('<int:id>/<slug:slug>/', views.product_detail,name='product_detail'),
]
