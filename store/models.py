from django.db import models

class Clients(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    @staticmethod
    def get_clients(params=None):
        clients = Clients.objects.all()
        data_serializer = [{
            "id": client.id,
            "last_name": client.last_name,
            "first_name": client.first_name,
            "patronymic": client.patronymic,
            "address": client.address
        } for client in clients]
        return data_serializer

    @staticmethod
    def get_clients_name(params=None):
        client_data = Clients.objects.all()
        data_serializer = [{"name": client.__str__(), "id": client.id} for client in client_data]
        return data_serializer

    @staticmethod
    def add_client(request_data):
        clients = Clients(last_name=request_data["last_name"], first_name=request_data["first_name"],
                          patronymic=request_data["patronymic"], address=request_data["address"])
        clients.save()
        return 'Успешное добавление клиента'

    @staticmethod
    def change_client(request_data):
        current_client = Clients.objects.get(pk=request_data["id"])
        current_client.last_name = request_data["last_name"]
        current_client.first_name = request_data["first_name"]
        current_client.patronymic = request_data["patronymic"]
        current_client.address = request_data["address"]
        current_client.save()
        return 'Успешное изменения клиента'


class Groups(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def get_groups(params=None):
        groups = Groups.objects.all()
        data_serializer = [{"id": group.id, "title": group.title} for group in groups]
        return data_serializer


class Manufacturers(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def get_manufacturers(params=None):
        manufacturers = Manufacturers.objects.all()
        data_serializer = [{"id": manufacturer.id, "title": manufacturer.title} for manufacturer in manufacturers]
        return data_serializer


class Nomenclature(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    count = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_nomenclature(params=None):
        nomenclature = Nomenclature.objects.all()
        data_serializer = [{
            "id": nomenclatur.id,
            "title": nomenclatur.title,
            "manufacturer": nomenclatur.manufacturer.title,
            "group": nomenclatur.group.title,
            "description": nomenclatur.description,
            "price": nomenclatur.price,
            "count": nomenclatur.count
        } for nomenclatur in nomenclature]
        return data_serializer

    @staticmethod
    def add_nomenclature(request_data):
        nomenclature = Nomenclature(title=request_data["title"],
                                    manufacturer=Manufacturers.objects.get(pk=request_data["manufacturer"]),
                                    group=Groups.objects.get(pk=request_data["group"]),
                                    description=request_data["description"],
                                    price=request_data["price"],
                                    count=request_data["count"])
        nomenclature.save()
        return 'Успешное добавление товара'

    @staticmethod
    def change_nomenclature(request_data):
        current_nomenclature = Nomenclature.objects.get(pk=request_data["id"])
        current_nomenclature.title = request_data["title"]
        current_nomenclature.manufacturer = Manufacturers.objects.get(pk=request_data["manufacturer"])
        current_nomenclature.group = Groups.objects.get(pk=request_data["group"])
        current_nomenclature.description = request_data["description"]
        current_nomenclature.price = request_data["price"]
        current_nomenclature.count = request_data["count"]
        current_nomenclature.save()
        return 'Успешное изменение товара'

class Products(models.Model):
    nomenclature = models.ForeignKey(Nomenclature, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()

    def __str__(self):
        return self.nomenclature.title

    @staticmethod
    def get_products(params=None):
        products = Products.objects.all()
        data_serializer = [{
            "id": product.id,
            "title": product.nomenclature.title,
            "group": product.nomenclature.group.title,
            "manufacturer": product.nomenclature.manufacturer.title,
            "description": product.nomenclature.description,
            "price": product.price,
            "count": product.count
        } for product in products]
        return data_serializer


class Orders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    date_time = models.DateTimeField(auto_now_add=True)

    COMPLETED = 'Выполнен'
    CANCELLED = 'Отменён'
    PAID = 'Оплачен'
    NEW = 'Новый'
    status_choices = [
        (COMPLETED, 'Выполнен'),
        (CANCELLED, 'Отменён'),
        (PAID, 'Оплачен'),
        (NEW, 'Новый')
    ]
    status = models.CharField(max_length=50, choices=status_choices, default=NEW)

    def __str__(self):
        return f'Номер заказа: {self.id}'

    @staticmethod
    def get_orders(params=None):
        orders = Orders.objects.all().filter(status="Новый")
        data_serializer = [{
            "id": order.id,
            "name_client": order.client.__str__(),
            "client_address": order.client.address,
            "date_time": order.date_time.strftime('%H:%M %Y.%m.%d'),
            "status": order.status
        } for order in orders]
        return data_serializer

    @staticmethod
    def get_current_products(request_data):
        current_order = Orders.objects.get(pk=request_data["pk"])
        data_serializer = {
            "product": [{
                "id": i.id,
                "title": i.nomenclature.title,
                "manufacturer": i.nomenclature.manufacturer.title,
                "group": i.nomenclature.group.title,
                "price": i.price,
                "count": i.count
            } for i in current_order.products.all()]
        }
        return data_serializer

    @staticmethod
    def add_order(request_data):
        product = []
        for data in request_data["products"]:
            if data["count"] <= Nomenclature.objects.get(pk=data["id"]).count:
                b = Nomenclature.objects.get(pk=data["id"])
                b.count -= data["count"]
                b.save()
                product.append(Products.objects.create(nomenclature_id=data["id"], price=data["price"],
                                                       count=data["count"]))
            else:
                print("Товаров на остатке меньше")
                continue
        order = Orders.objects.create(client=Clients.objects.get(pk=request_data["client"]))
        order.products.set(product)
        order.save()
        return 'Успешное создание заказа'

    @staticmethod
    def cancel_order(request_data):
        current_order = Orders.objects.get(pk=request_data["id"])
        current_order.status = request_data["status"]
        current_order.save()
        return 'Заказ отменён'

    @staticmethod
    def completed_order(request_data):
        current_order = Orders.objects.get(pk=request_data["id"])
        current_order.status = request_data["status"]
        current_order.save()
        return 'Заказ исполнен'


    @staticmethod
    def change_order(request_data):
        current_product = Products.objects.get(pk=request_data["id"])
        сhange = int(request_data["count"]) - current_product.count
        current_count_fact = Nomenclature.objects.get(pk=current_product.nomenclature.id)
        if сhange > 0:
            if сhange <= current_count_fact.count:
                current_count_fact.count -= сhange
                current_count_fact.save()
                current_product.count += сhange
                current_product.save()
            else:
                print('на стока увеличить низзя')
        elif сhange == 0:
            print('0 есть 0')
        else:
            current_product.count - сhange
            if current_product.count <= 0:
                print('Надо уже удалять тогда')
            else:
                current_product.save()