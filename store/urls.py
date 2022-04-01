from django.urls import path
from store import views

urlpatterns = [
    path('api/clients', views.get_clients_list),
    path('api/groups', views.get_groups_list),
    path('api/manufacturers', views.get_manufacturers_list),
    path('api/nomenclature', views.get_nomenclature_list),
    path('api/products', views.get_products_list),
    path('api/orders', views.get_orders_list),
    path('api/current-product', views.get_current_products),
    path('api/order-add', views.get_order_add),
]