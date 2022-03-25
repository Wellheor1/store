"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls'))
]

# urlpatterns += router.urls
