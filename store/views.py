import json

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Products, Clients, Groups, Nomenclature, Manufacturers, Orders


@csrf_exempt
def get_clients_list(request):
    data_serializer = Clients.get_clients()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_groups_list(request):
    data_serializer = Groups.get_groups()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_manufacturers_list(request):
    data_serializer = Manufacturers.get_manufacturer()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_nomenclature_list(request):
    data_serializer = Nomenclature.get_nomenclature()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_products_list(request):
    data_serializer = Products.get_products()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_orders_list(request):
    data_serializer = Orders.get_orders()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_current_products(request):
    request_data = json.loads(request.body)
    current_products = Orders.objects.get(id=request_data["pk"])
    data = {
        "product": [{
            "id": i.nomenclature.id,
            "title": i.nomenclature.title,
            "manufacturer": i.nomenclature.manufacturer.title,
            "group": i.nomenclature.group.title,
            "price": i.price,
            "count": i.count
        } for i in current_products.products.all()]
    }
    return JsonResponse(data)

@csrf_exempt
def get_order_add(request):
    product_data = Products.objects.all()
    data_serializer = []
    for product in product_data:
        data_serializer.append(
            {
                
            }
        )
            # "children": [
            #     {
            #         "id": product.nomenclature.manufacturer.id,
            #         "name": product.nomenclature.manufacturer.title,
            #         "Children": [
            #             {
            #                 "id": product.nomenclature.id,
            #                 "name": product.nomenclature.title
            #             }
            #         ]
            #     }
            # ]
    return JsonResponse(data_serializer, safe=False)
