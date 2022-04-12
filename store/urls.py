from django.urls import path
from store import views

urlpatterns = [
    path('api/clients', views.get_clients_list),
    path('api/clients-name', views.get_clients_name),
    path('api/add-client', views.add_client),
    path('api/change-client', views.change_client),
    path('api/groups', views.get_groups_list),
    path('api/manufacturers', views.get_manufacturers_list),
    path('api/nomenclature', views.get_nomenclature_list),
    path('api/add-nomenclature', views.add_nomenclature),
    path('api/change-nomenclature', views.change_nomenclature),
    path('api/products', views.get_products_list),
    path('api/current-product', views.get_current_products),
    path('api/orders', views.get_orders_list),
    path('api/cancel-order', views.cancel_order),
    path('api/completed-order', views.completed_order),
    path('api/add-order', views.add_order),
    path('api/change-order', views.change_order)
]