from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    patronymic = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'


class Type(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Manufacturer(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Model(models.Model):
    title = models.CharField(max_length=255)
    manufacturer_id = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


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
                "type_id": product.type_id.id,
                "model_id": product.model_id.id,
                "manufacturer_id": product.manufacturer_id.id,
                "description": product.description,
                "price": product.price
            })
        return data_serializer




class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'Номер заказа: {self.id} {Product.title}'