from django.urls import path
from myapp import views

urlpatterns = [
    path('api/customer', views.get_customer_list),
    path('api/type', views.get_type_list),
    path('api/manufacturer', views.get_manufacturer_list),
    path('api/model', views.get_model_list),
    path('api/product', views.get_product_list),
    path('api/order', views.get_order_list),
]