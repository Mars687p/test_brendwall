
from rest_framework import serializers

from .models import Products


class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class GetProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
