from django.urls import path, include
from django.contrib.auth import get_user_model
from .serializers import ProductosSerializer
from shop.models import Productos
from rest_framework import serializers, viewsets, routers
from rest_framework.routers import DefaultRouter
# Serializers define the API representation.

User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = DefaultRouter()
router.register('productos', ProductosViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls), name="index"),
    path('api/', include(router.urls), name="api"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + router.urls
