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
def get_product_tree(request):
    product_data = Products.objects.all()
    id = 1
    prev_group_pk = None
    result = []
    tmp_group = {
            "id": "",
            "name": "",
            "children": [
                {
                    "id": "",
                    "name": "",
                    "children": [
                        {
                            "id": "",
                            "name": ""
                        }
                    ]
                }
            ]
        }

    step = 0
    for product in product_data:
        groups_pks = [k["id"] for k in result]
        if product.nomenclature.group.pk not in groups_pks:
            if step != 0:
                result.append(tmp_group.copy())
            tmp_group["id"] = product.nomenclature.group.pk
            tmp_group["name"] = product.nomenclature.group.title
            tmp_group["children"] = [
                        {
                            "id": product.nomenclature.manufacturer.pk,
                            "name": product.nomenclature.manufacturer.title
                        }
                    ]

        tmp_children_general = tmp_group["children"]
        manufacture_pks = [k["id"] for k in tmp_children_general]
        if product.nomenclature.manufacturer.pk not in manufacture_pks:
            tmp_children_slave = {}
            tmp_children_slave["id"] = product.nomenclature.manufacturer.pk
            tmp_children_slave["name"] = product.nomenclature.manufacturer.title
            tmp_children_general.append(tmp_children_skave.copy())

        tmp_group["children"] = tmp_children_general.copy()
        prev_group_pk = product.nomenclature.group.pk
        step += 1
 
    result.append(tmp_group.copy())
    for i in result:
        print(i)

    return JsonResponse(result, safe=False)
