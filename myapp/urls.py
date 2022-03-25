from django.contrib import admin
from django.urls import path, include
# from myapp.views import CustomerView
# from myapp.views import ProductView
# from myapp.views import TypeView
# from myapp.views import ModelView
# from myapp.views import ManufacturerView
# from myapp.views import OrderView


from rest_framework.routers import SimpleRouter

#router = SimpleRouter()
#router.register('api/customer', CustomerView)
#router.register('api/product', ProductView)
#router.register('api/type', TypeView)
#router.register('api/model', ModelView)
#router.register('api/manufacturer', ManufacturerView)
#router.register('api/order', OrderView)

#urlpatterns = router.urls
from myapp import views

urlpatterns = [
    #path('api/customer', views.CustomerApi),
    #path('api/customer/<int:id>', views.CustomerApi),
    path('api/product', views.ProductView.as_view()),
    #path('api/product/<int:pk>', views.Product_detail),
    #path('api/order', views.OrderApi),
    #path('api/order/<int:id>', views.OrderApi),
]