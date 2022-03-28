from django.contrib import admin
from .models import Products, Clients, Groups, Nomenclature, Manufacturers, Orders

# Register your models here.
admin.site.register(Clients)
admin.site.register(Products)
admin.site.register(Groups)
admin.site.register(Nomenclature)
admin.site.register(Manufacturers)
admin.site.register(Orders)