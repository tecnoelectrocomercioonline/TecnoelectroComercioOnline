from rest_framework import serializers
from shop.models import Productos


class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productos
        # fields =  ['title', 'capacity', 'description', 'price', 'category', 'productphoto']
        fields = '__all__'
