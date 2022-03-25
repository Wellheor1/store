from django.urls import path
from myapp import views

urlpatterns = [
    path('api/product', views.get_product_list)
]