from django.db import models


class Clients(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    patronymic = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

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
        for nomenclatur in nomenclature:
            data_serializer.append({
                "id": nomenclatur.id,
                "title": nomenclatur.title,
                "manufacturer": nomenclatur.manufacturer.title,
                "group": nomenclatur.group.title,
                "description": nomenclatur.description
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
                "group": product.nomenclature.group,
                "manufacturer": product.nomenclature.manufacturer,
                "description": product.nomenclature.description,
                "price": product.price,
                "count": products.count
            })
        return data_serializer


class Orders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'Номер заказа: {self.id}'

    @staticmethod
    def get_orders(params=None):
        orders = Orders.objects.all()
        data_serializer = []
        for order in orders:
            data_serializer.append({
                "id": order.id,
                "customer_last_name": order.customer_id.last_name,
                "customer_first_name": order.customer_id.first_name,
                "customer_patronymic": order.customer_id.patronymic,
                #"products": order.products,
                "date_time": order.date_time.strftime('%H:%M %Y.%m.%d')
            })
        return data_serializer
