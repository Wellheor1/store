from django.urls import path
from store import views

urlpatterns = [
    path('clients', views.get_clients_list),
    path('clients-name', views.get_clients_name),
    path('add-client', views.add_client),
    path('change-client', views.change_client),
    path('groups', views.get_groups_list),
    path('manufacturers', views.get_manufacturers_list),
    path('nomenclature', views.get_nomenclature_list),
    path('add-nomenclature', views.add_nomenclature),
    path('change-nomenclature', views.change_nomenclature),
    path('products', views.get_products_list),
    path('current-product', views.get_current_products),
    path('delete-current-product', views.delete_current_product),
    path('orders', views.get_orders_list),
    path('cancel-order', views.cancel_order),
    path('completed-order', views.completed_order),
    path('add-order', views.add_order),
    path('change-count-product-order', views.change_count_product_order)
]