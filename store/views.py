import json

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Products, Clients, Groups, Nomenclature, Manufacturers, Orders


@csrf_exempt
def get_clients_list(request):
    data_serializer = Clients.get_clients()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_clients_name(request):
    data_serializer = Clients.get_clients_name()
    return JsonResponse(data_serializer, safe=False)


@csrf_exempt
def add_client(request):
    request_data = json.loads(request.body)
    Clients.add_client(request_data)
    return JsonResponse('Успешное добавление заказа', safe=False)


@csrf_exempt
def change_client(request):
    request_data = json.loads(request.body)
    Clients.change_client(request_data)
    return JsonResponse('Успешное изменение клиента', safe=False)


@csrf_exempt
def get_groups_list(request):
    data_serializer = Groups.get_groups()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_manufacturers_list(request):
    data_serializer = Manufacturers.get_manufacturers()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def get_nomenclature_list(request):
    data_serializer = Nomenclature.get_nomenclature()
    return JsonResponse({"data": data_serializer})


@csrf_exempt
def add_nomenclature(request):
    request_data = json.loads(request.body)
    Nomenclature.add_nomenclature(request_data)
    return JsonResponse('Успешное добавление товара', safe=False)


@csrf_exempt
def change_nomenclature(request):
    request_data = json.loads(request.body)
    Nomenclature.change_nomenclature(request_data)
    return JsonResponse('Успешное изменение товара', safe=False)


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
    data_serializer = Orders.get_current_products(request_data)
    return JsonResponse(data_serializer)


@csrf_exempt
def add_order(request):
    request_data = json.loads(request.body)
    Orders.add_order(request_data)
    return JsonResponse('Успешное добавление заказа', safe=False)


@csrf_exempt
def cancel_order(request):
    request_data = json.loads(request.body)
    Orders.cancel_order(request_data)
    return JsonResponse('Заказ отменён', safe=False)


@csrf_exempt
def completed_order(request):
    request_data = json.loads(request.body)
    Orders.completed_order(request_data)
    return JsonResponse('Заказ исполнен', safe=False)


@csrf_exempt
def change_order(request):
    request_data = json.loads(request.body)
    Orders.change_order(request_data)
    return JsonResponse('Заказ изменён', safe=False)

