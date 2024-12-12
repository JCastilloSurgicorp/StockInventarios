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
            'id':['exact'],
            'nro_guia':['exact', 'contains'], 
            'status_picking':['exact'],
            'lima_provincia':['exact'],
            'empr_id':['exact'],
            'tipo_pedido':['exact'],
            'atencion':['exact', 'contains'], 
            'fecha_atencion':['exact', 'lte', 'gte'], 
            'ubicacion_sector':['exact', 'contains'],
        }                                                                                                                                                                                                                                                                  