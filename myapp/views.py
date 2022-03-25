from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Product, Customer, Type, Model, Manufacturer, Order


@csrf_exempt
def get_product_list(request):
    data_serializer = Product.get_product()

    return JsonResponse({"data": data_serializer})





