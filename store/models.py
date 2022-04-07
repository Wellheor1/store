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

    def get_orders(params=None):
        orders = Orders.objects.all()
        data_serializer = [{
            "id": order.id,
            "name_client": order.client.__str__(),
            "client_address": order.client.address,
            "date_time": order.date_time.strftime('%H:%M %Y.%m.%d'),
            "status": order.status
        } for order in orders]
        return data_serializer
