from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SI_LineaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SI_Linea
        fields = '__all__'

class SI_GrupoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SI_Grupo
        fields = '__all__'

class SI_ProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SI_Productos
        fields = '__all__'

class SI_TipoProductosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SI_TipoProductos
        fields = '__all__'

class SI_EmpresaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SI_Empresa
        fields = '__all__'

class SI_DepositosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SI_Depositos
        fields = '__all__'

class SI_TipoAlmacenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SI_TipoAlmacen
        fields = '__all__'

class SI_SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SI_Sector
        fields = '__all__'

class StocksInventarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StocksInventario
        fields = '__all__'