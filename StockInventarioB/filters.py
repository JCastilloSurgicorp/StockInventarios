from rest_framework import permissions, viewsets, filters
import django_filters.rest_framework as df
import django_filters
from django.shortcuts import render
from .serializers import *
from .models import *


class HojaPickingFilter(django_filters.FilterSet):
    class Meta:
        model = HojaPicking
        fields = {
            'id':['iexact'],
            'nro_guia':['iexact', 'icontains'],
            'status_picking':['iexact'],
            'lima_provincia':['iexact'],
            'empr_id':['iexact'],
            'tipo_pedido':['iexact'],
            'atencion':['iexact', 'icontains'],
            'fecha_atencion':['exact', 'lt', 'gt', 'range'],
            'ubicacion_sector':['iexact', 'icontains'],
        }
