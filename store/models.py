from django.db import models


class Clients(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    patronymic = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    @staticmethod
    def get_clients(params=None):
        clients = Clients.objects.all()
        data_serializer = []
        for client in clients:
            data_serializer.append({
                "id": client.id,
                "last_name": client.last_name,
                "first_name": client.first_name,
                "patronymic": client.patronymic,
                "address": client.address
            })
        return data_serializer

    # @staticmethod
    # def put_clients(params=None):


class Groups(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def get_groups(params=None):
        groups = Groups.objects.all()
        data_serializer = []
        for group in groups:
            data_serializer.append({
                "id": group.id,
                "title": group.title,
            })
        return data_serializer


class Manufacturers(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def get_manufacturers(params=None):
        manufacturers = Manufacturers.objects.all()
        data_serializer = []
        for manufacturer in manufacturers:
            data_serializer.append({
                "id": manufacturer.id,
                "title": manufacturer.title,
            })
        return data_serializer


class Nomenclature(models.Model):
    title = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def get_nomenclature(params=None):
        nomenclature = Nomenclature.objects.all()
        data_serializer = []
        for nomenclatu in nomenclature:
            data_serializer.append({
                "id": nomenclatu.id,
                "title": nomenclatu.title,
                "manufacturer": nomenclatu.manufacturer.title,
                "group": nomenclatu.group.title,
                "description": nomenclatu.description
            })
        return data_serializer


class Products(models.Model):
    nomenclature = models.ForeignKey(Nomenclature, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()

    def __str__(self):
        return self.nomenclature.title

    @staticmethod
    def get_products(params=None):
        products = Products.objects.all()
        data_serializer = []
        for product in products:
            data_serializer.append({
                "id": product.id,
                "title": product.nomenclature.title,
                "group": product.nomenclature.group.title,
                "manufacturer": product.nomenclature.manufacturer.title,
                "description": product.nomenclature.description,
                "price": product.price,
                "count": product.count
            })
        return data_serializer


class Orders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'Номер заказа: {self.id}'

    def get_orders(params=None):
        orders = Orders.objects.all()
        data_serializer = []
        for order in orders:
            data_serializer.append({
                "id": order.id,
                "name_client": order.client.__str__(),
                "client_address": order.client.address,
                "products": [
                    {
                        "id": i.nomenclature.id,
                        "title": i.nomenclature.title,
                        "manufacturer": i.nomenclature.manufacturer.title,
                        "group": i.nomenclature.group.title,
                        "price": i.price,
                        "count": i.count
                    } for i in order.products.all()],
                "date_time": order.date_time.strftime('%H:%M %Y.%m.%d'),
            })
        return data_serializer
