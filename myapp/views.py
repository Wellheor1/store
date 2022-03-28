from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Product, Customer, Type, Model, Manufacturer, Order


@csrf_exempt
def get_customer_list(request):
    data_serializer = Customer.get_customer()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_type_list(request):
    data_serializer = Type.get_type()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_manufacturer_list(request):
    data_serializer = Manufacturer.get_manufacturer()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_model_list(request):
    data_serializer = Model.get_model()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_product_list(request):
    data_serializer = Product.get_product()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_order_list(request):
    data_serializer = Order.get_order()
    return JsonResponse({"data": data_serializer})
