from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import json
from .models import Product, Customer, Type, Model, Manufacturer, Order


# from myapp.models import products
# from myapp.serializers import productSerializer
#
# from django.core.files.storage import default_storage
#
@csrf_exempt
class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        data = []
        for product in products:
            data.append({
                'title': product.title,
                'type_id': product.type_id,
                'model_id': product.model_id,
                'manufacturer_id': product.manufacturer_id,
                'description': product.description,
                'price': product.price
            })
        return JsonResponse(data)


    # def Get_Product_list(request):
    #     request_data = json.loads(request.body)
    #     print(request_data)
    #     #product = Product.objects.all()
    #     return JsonResponse(request_data, safe=False)


# @csrf_exempt
# def SaveFile(request):
#     file = request.FILES['file']
#     file_name = default_storage.save(file.name,file)
#     return JsonResponse(file_name, safe=False)


# class CustomerView(ModelViewSet):
#     queryset = Customer.objects.all().values()
#     serializer_class = CustomerSerializer
#
#
# class ProductView(ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class TypeView(ModelViewSet):
#     queryset = Type.objects.all()
#     serializer_class = TypeSerializer
#
#
# class ModelView(ModelViewSet):
#     queryset = Model.objects.all()
#     serializer_class = ModelSerializer
#
#
# class ManufacturerView(ModelViewSet):
#     queryset = Manufacturer.objects.all()
#     serializer_class = ManufacturerSerializer
#
#
# class OrderView(ModelViewSet):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
