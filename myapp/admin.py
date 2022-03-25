from django.contrib import admin
from .models import Product, Customer, Type, Model, Manufacturer, Order

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Type)
admin.site.register(Model)
admin.site.register(Manufacturer)
admin.site.register(Order)