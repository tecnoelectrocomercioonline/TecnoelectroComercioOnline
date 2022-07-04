from rest_framework import serializers
from shop.models import Productos
from authentication.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productos
        # fields =  ['title', 'capacity', 'description', 'price', 'category', 'productphoto']
        fields = '__all__'
