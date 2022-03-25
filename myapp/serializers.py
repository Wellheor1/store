from rest_framework import serializers
from .models import Product, Customer, Manufacturer, Type, Model, Order


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'patronymic', 'address')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'title')


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'title')


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ('id', 'title', 'manufacturer_id')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'type_id', 'model_id', 'manufacturer_id', 'description', 'price')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'products', 'date_time')
