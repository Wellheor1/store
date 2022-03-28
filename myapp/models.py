import datetime

import ins as ins
import products.products
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    patronymic = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'

    @staticmethod
    def get_customer(params=None):
        customers = Customer.objects.all()
        data_serializer = []
        for customer in customers:
            data_serializer.append({
                "id": customer.id,
                "last_name": customer.last_name,
                "first_name": customer.first_name,
                "patronymic": customer.patronymic,
                "address": customer.address
            })
        return data_serializer


class Type(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def get_type(params=None):
        types = Type.objects.all()
        data_serializer = []
        for type in types:
            data_serializer.append({
                "id": type.id,
                "title": type.title,
            })
        return data_serializer


class Manufacturer(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    @staticmethod
    def get_manufacturer(params=None):
        manufacturers = Manufacturer.objects.all()
        data_serializer = []
        for manufacturer in manufacturers:
            data_serializer.append({
                "id": manufacturer.id,
                "title": manufacturer.title,
            })
        return data_serializer


class Model(models.Model):
    title = models.CharField(max_length=255)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @staticmethod
    def get_model(params=None):
        models = Model.objects.all()
        data_serializer = []
        for model in models:
            data_serializer.append({
                "id": model.id,
                "title": model.title,
                "manufacturer_id": model.manufacturer_id.title
            })
        return data_serializer


class Product(models.Model):
    title = models.CharField(max_length=255)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    model_id = models.ForeignKey(Model, on_delete=models.CASCADE)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    @staticmethod
    def get_product(params=None):
        products = Product.objects.all()
        data_serializer = []
        for product in products:
            data_serializer.append({
                "id": product.id,
                "title": product.title,
                "type_id": product.type_id.title,
                "model_id": product.model_id.title,
                "manufacturer_id": product.manufacturer_id.title,
                "description": product.description,
                "price": product.price
            })
        return data_serializer


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'Номер заказа: {self.id}'

    @staticmethod
    def get_order(params=None):
        orders = Order.objects.all()
        data_serializer = []
        for order in orders:
            data_serializer.append({
                "id": order.id,
                "customer_last_name": order.customer_id.last_name,
                "customer_first_name": order.customer_id.first_name,
                "customer_patronymic": order.customer_id.patronymic,
                "products": order.products,
                "date_time": order.date_time.strftime('%H:%M %Y.%m.%d')
            })
        print(data_serializer)
        return data_serializer
