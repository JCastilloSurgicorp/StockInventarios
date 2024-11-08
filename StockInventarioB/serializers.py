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

class HP_ProveedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HP_Proveedor
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

class GuiasRemisionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GuiasRemision
        fields = '__all__'

class GR_DescripcionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GR_Descripcion
        fields = '__all__'

class GuiasRemision_OCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GuiasRemision_OC
        fields = '__all__'

class GR_Descripcion_OCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GR_Descripcion_OC
        fields = '__all__'

class GR_BusquedaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GR_Busqueda
        fields = '__all__'

class Fact_BusquedaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fact_Busqueda
        fields = '__all__'

class Fact_DetalleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fact_Detalle
        fields = '__all__'

class HojaPickingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HojaPicking
        fields = '__all__'

class Pend_GuiasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pend_Guias
        fields = '__all__'

class Pend_ItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pend_Items
        fields = '__all__'