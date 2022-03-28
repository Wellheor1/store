import json

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Products, Clients, Groups, Nomenclature, Manufacturers, Orders


@csrf_exempt
def get_clients_list(request):
    data_serializer = Clients.get_clients()
    return JsonResponse({"data": data_serializer})

@csrf_exempt
def put_clients(request):
    request_data = json.loads(request.body)
    data = Clients.objects.filter(id=request_data["id"])
    data1 = []
    print(data)
    # for i in data:
    #     data1.append({
    #         "id": data.id
    #     })
    # #data.save()

    #data[0] = request_data
    #print(data)
    #data.save()
    #return JsonResponse("Всё обновилось", data)


# @csrf_exempt
# def post_client(request):
#     request_data = json.loads(request.body)



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
