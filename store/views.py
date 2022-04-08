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
    data_serializer = Manufacturers.get_manufacturers()
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
    current_products = Orders.objects.get(pk=request_data["pk"])
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
def get_clients_name(request):
    client_data = Clients.objects.all()
    data = [{"name": client.__str__(), "id": client.id} for client in client_data]
    return JsonResponse(data, safe=False)


@csrf_exempt
def add_order(request):
    request_data = json.loads(request.body)
    products = [Products.objects.get(pk=data["id"]) for data in request_data["products"]]
    print(products)
    order = Orders.objects.create(client=Clients.objects.get(pk=request_data["client"]))
    #order.products.set(products)
    #order.save()
    return JsonResponse('Успешное создание заказа', safe=False)


@csrf_exempt
def add_client(request):
    request_data = json.loads(request.body)
    print(request_data)
    clients = Clients(last_name=request_data["last_name"], first_name=request_data["first_name"],
                     patronymic=request_data["patronymic"], address=request_data["address"])
    clients.save()
    return JsonResponse('Успешное добавление клиента', safe=False)


@csrf_exempt
def add_nomenclature(request):
    request_data = json.loads(request.body)
    print(request_data)
    nomenclature = Nomenclature(title=request_data["title"],
                                manufacturer=Manufacturers.objects.get(pk=request_data["manufacturer"]),
                                group=Groups.objects.get(pk=request_data["group"]),
                                description=request_data["description"],
                                price=request_data["price"],
                                count=request_data["count"])
    nomenclature.save()
    return JsonResponse('Успешное добавление товара', safe=False)


@csrf_exempt
def change_client(request):
    request_data = json.loads(request.body)
    current_client = Clients.objects.get(pk=request_data["id"])
    current_client.last_name = request_data["last_name"]
    current_client.first_name = request_data["first_name"]
    current_client.patronymic = request_data["patronymic"]
    current_client.address = request_data["address"]
    current_client.save()
    return JsonResponse('Успешное изменение клиента', safe=False)


@csrf_exempt
def change_nomenclature(request):
    request_data = json.loads(request.body)
    current_nomenclature = Nomenclature.objects.get(pk=request_data["id"])
    current_nomenclature.title = request_data["title"]
    current_nomenclature.manufacturer = Manufacturers.objects.get(pk=request_data["manufacturer"])
    current_nomenclature.group = Groups.objects.get(pk=request_data["group"])
    current_nomenclature.description = request_data["description"]
    current_nomenclature.price = request_data["price"]
    current_nomenclature.count = request_data["count"]
    current_nomenclature.save()
    return JsonResponse('Успешное изменение товара', safe=False)


@csrf_exempt
def cancel_order(request):
    request_data = json.loads(request.body)
    current_order = Orders.objects.get(pk=request_data["id"])
    current_order.status = request_data["status"]
    current_order.save()
    return JsonResponse('Заказ отменён', safe=False)

@csrf_exempt
def completed_order(request):
    request_data = json.loads(request.body)
    current_order = Orders.objects.get(pk=request_data["id"])
    current_order.status = request_data["status"]
    current_order.save()
    return JsonResponse('Заказ исполнен', safe=False)