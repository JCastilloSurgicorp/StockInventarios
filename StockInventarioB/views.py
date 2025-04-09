from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions, viewsets, filters
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import Group, User
from AsistVirtual.onnx_inference import generate_suggestion
from rest_framework.decorators import action
from rest_framework.response import Response
import django_filters.rest_framework as df
from rest_framework.views import APIView
from datetime import datetime, timezone
from pdf2image import convert_from_path
from django.shortcuts import render
from rest_framework import status
from django.db.models import Sum
from PIL import Image, ImageWin
from pythonwin import win32ui
from win32 import win32print
from .serializers import *
from .filters import *
from .models import *
from fpdf import FPDF
import subprocess
import time
import os


def Question(request):
    return render(request, 'SIB/index.html')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.DjangoModelPermissions]
        else:
            permission_classes = [permissions.DjangoModelPermissions]
        return [permission() for permission in permission_classes]
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [df.DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['id', 'username', 'first_name', 'last_name','email']
    permission_classes = get_permissions

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.DjangoModelPermissions]
        return [permission() for permission in permission_classes]
    
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = get_permissions

class SI_LineaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = SI_Linea.objects.all().order_by('id')
    serializer_class = SI_LineaSerializer
    permission_classes = get_permissions

class SI_GrupoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = SI_Grupo.objects.all().order_by('id')
    serializer_class = SI_GrupoSerializer
    permission_classes = get_permissions

class HP_ProveedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = HP_Proveedor.objects.all().order_by('id')
    serializer_class = HP_ProveedorSerializer
    permission_classes = get_permissions

class SI_ProductosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = SI_Productos.objects.all().order_by('id')
    serializer_class = SI_ProductosSerializer
    permission_classes = get_permissions

class SI_TipoProductosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = SI_TipoProductos.objects.all().order_by('id')
    serializer_class = SI_TipoProductosSerializer
    permission_classes = get_permissions

class SI_EmpresaViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed 
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = SI_Empresa.objects.all().order_by('id')
    serializer_class = SI_EmpresaSerializer
    permission_classes = get_permissions

class SI_DepositosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = SI_Depositos.objects.all().order_by('id')
    serializer_class = SI_DepositosSerializer
    permission_classes = get_permissions

class SI_TipoAlmacenViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = SI_TipoAlmacen.objects.all().order_by('id')
    serializer_class = SI_TipoAlmacenSerializer
    permission_classes = get_permissions

class SI_SectorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = SI_Sector.objects.all().order_by('id')
    serializer_class = SI_SectorSerializer
    permission_classes = get_permissions

class StocksInventarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.DjangoModelPermissions]
        elif self.action == 'destroy':
            permission_classes = [permissions.DjangoModelPermissions]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = StocksInventario.objects.filter(stock__gt=0).order_by('-stock')
    filter_backends = [df.DjangoFilterBackend]
    serializer_class = StocksInventarioSerializer
    filterset_class = StocksInventarioFilter
    permission_classes = get_permissions

    @action(detail=False, methods=['GET'], url_path='resumen')
    def resumen(self, request):
        prod = request.query_params.get('descr_prod')
        productos = StocksInventario.objects.values('descr_prod').annotate(stock_total=Sum('stock')).filter(descr_prod__contains=prod, stock__gt=0).order_by('descr_prod')
        stock_string = ""
        for item in productos:
            stock_string = stock_string + f"{item['descr_prod']}:  \t{item['stock_total']} unidades,\n"
        stock_string = stock_string[:-2]
        if stock_string == "":
            return Response({'detail': f'No tenemos stock de {prod} Actualmente.\nDesea consultar sobre otro producto?'}, status=status.HTTP_200_OK)
        return Response({'message': f'Tenemos los siguiente productos {prod} en stock: \n\n{stock_string}\n\nDesea consultar sobre algún otro producto?'}, status=status.HTTP_200_OK)

class GuiasRemisionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.DjangoModelPermissions]
        elif self.action == 'destroy':
            permission_classes = [permissions.DjangoModelPermissions]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = GuiasRemision.objects.all().order_by('id')
    serializer_class = GuiasRemisionSerializer
    filter_backends = [df.DjangoFilterBackend]
    filterset_fields = ['nro_guia','empresa']
    permission_classes = get_permissions

class GR_DescripcionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.DjangoModelPermissions]
        elif self.action == 'destroy':
            permission_classes = [permissions.DjangoModelPermissions]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = GR_Descripcion.objects.all().order_by('-id')
    serializer_class = GR_DescripcionSerializer
    filter_backends = [df.DjangoFilterBackend]
    filterset_fields = ['nro_guia','empr_id']
    permission_classes = get_permissions

class GuiasRemision_OCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = GuiasRemision_OC.objects.all().order_by('-id')
    serializer_class = GuiasRemision_OCSerializer
    filter_backends = [df.DjangoFilterBackend]
    filterset_fields = ['nro_guia','empresa']
    permission_classes = get_permissions

class GR_Descripcion_OCViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == 'retrieve':
            permission_classes = [permissions.DjangoModelPermissions]
        elif self.action == 'destroy':
            permission_classes = [permissions.DjangoModelPermissions]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = GR_Descripcion_OC.objects.all().order_by('id')
    serializer_class = GR_Descripcion_OCSerializer
    filter_backends = [df.DjangoFilterBackend]
    filterset_fields = ['id','nro_guia','empr_id']
    permission_classes = get_permissions

class GR_BusquedaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = GR_Busqueda.objects.all().order_by('id')
    serializer_class = GR_BusquedaSerializer
    permission_classes = get_permissions

class Fact_BusquedaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = Fact_Busqueda.objects.all().order_by('-id')
    serializer_class = Fact_BusquedaSerializer
    permission_classes = get_permissions

class Fact_DetalleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = Fact_Detalle.objects.all().order_by('-id')
    serializer_class = Fact_DetalleSerializer
    permission_classes = get_permissions

class HojaPickingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.DjangoModelPermissions]
        return [permission() for permission in permission_classes]
    
    queryset = HojaPicking.objects.all().order_by('-id')
    serializer_class = HojaPickingSerializer
    filter_backends = [df.DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    pagination_class = PageNumberPagination
    pagination_class.page_size_query_param = 'top'
    pagination_class.max_page_size = 1000
    filterset_class = HojaPickingFilter
    permission_classes = get_permissions

    def partial_update(self, request, *args, **kwargs):
        record = self.get_object()
        SelectedRecord = self.get_serializer(record).data
        usuario_actual = request.user
        nombre_usuario = usuario_actual.first_name + ' ' + usuario_actual.last_name
        nuevo_estado = request.data.get("status_picking")
        try:
            # Verificar si el estado actual es "Picking En Proceso"
            if nuevo_estado == "Picking En Proceso" and SelectedRecord['status_picking'] == "Picking En Proceso":
                if SelectedRecord['almacen'] == nombre_usuario:
                    record.fecha_almacen = request.data.get("fecha_almacen")
                    record.save()
                    msj = f"Se Reinició el Proceso de Picking - {record.fecha_almacen}"
                    return Response({"detail": msj}, status=status.HTTP_200_OK)
                msj = f"No se puede cambiar el estado a {SelectedRecord['status_picking']}. Ya fue cambiado por {SelectedRecord['almacen']} el día {SelectedRecord['fecha_almacen']}"
                return Response({"detail": msj}, status=status.HTTP_400_BAD_REQUEST)
            # Verificar si el estado está cambiando a "Picking En Proceso" desde "Picking Pendiente"
            if nuevo_estado == "Picking En Proceso" and SelectedRecord['status_picking'] != "Picking Pendiente":
                msj = f"El estado solo puede cambiar de 'Picking Pendiente' a 'Picking En Proceso'. El estado actual es {SelectedRecord['status_picking']}"
                return Response({"detail": msj}, status=status.HTTP_400_BAD_REQUEST)
            # Verificar si el estado está cambiando a "Picking Terminado" y lo está cambiando el mismo usuario
            if nuevo_estado == "Picking Terminado" and SelectedRecord['almacen'] != nombre_usuario:
                msj = f"El estado solo se puede cambiar a {nuevo_estado} por {SelectedRecord['almacen']}."
                return Response({"detail": msj}, status=status.HTTP_400_BAD_REQUEST)
            # Continuar con la actualización si las validaciones pasan
            return super().partial_update(request, *args, **kwargs)
        except Exception as e:
            # Manejar errores inesperados
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['GET'])
    def print(self, request, pk=None):
        Record = self.get_object()
        SelectedRecord = self.get_serializer(Record).data
        empr_id = SelectedRecord['empr_id'][29]
        empresa_id = SI_Empresa.objects.get(id=empr_id)
        empresa = empresa_id.empresa
        if SelectedRecord['oc_cliente'] == '':
            gr_url = SelectedRecord['gr_id'][35:]
            gr_id = ''
            for letter in gr_url:
                if letter == '/':
                    break
                gr_id = gr_id + letter
            Guia = GuiasRemision.objects.get(id=gr_id)
            Descripcion = GR_Descripcion.objects.filter(nro_guia=SelectedRecord['nro_guia'], empr_id=empr_id)
        else:
            gr_url = SelectedRecord['gr_oc_id'][38:]
            gr_id = ''
            for letter in gr_url:
                if letter == '/':
                    break
                gr_id = gr_id + letter
            Guia = GuiasRemision_OC.objects.get(id=gr_id)
            Descripcion = GR_Descripcion_OC.objects.filter(nro_guia=SelectedRecord['nro_guia'], empr_id=empr_id)
        SelectedGuia = GuiasRemision_OCSerializer(Guia,context={'request': request}).data
        SelectedDescripcion = GR_Descripcion_OCSerializer(Descripcion, many=True,context={'request': request}).data
        sumCantidad = 0
        for record in SelectedDescripcion:
            sumCantidad = sumCantidad + int(float(record['cantidad']))
        filename = 'C:\\Users\\srvcaminitos\\Documents\\HP_tickets_pdf\\' + datetime.now().strftime("TICKET %Y-%m-%d_%H-%M-%S") + ".pdf"
        pdf = FPDF('P', 'mm', (80, 210))
        pdf.add_page()
        pdf.set_font(family="Arial", style="B", size=22)
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_y(pdf.get_y()-8)
        pdf.cell(w=60, h=6, txt=SelectedRecord['nro_guia'], align="C")
        pdf.ln()
        pdf.set_font_size(8)
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.set_draw_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.cell(w=60, h=6, txt=f"{empresa}", align="C")
        pdf.ln(h=10)            
        fecha_atencion = datetime.fromisoformat(SelectedRecord['fecha_atencion'])
        fecha_atencion = fecha_atencion.astimezone(timezone.utc).strftime('%d/%m/%Y %I:%M:%S %p')
        fecha_cx = datetime.fromisoformat(SelectedGuia['fecha_cirugia'])
        fecha_cx = fecha_cx.astimezone(timezone.utc).strftime('%d/%m/%Y')
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.set_font_size(6)
        pdf.cell(w=12, h=6, txt=f"Fecha:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.set_font_size(6.8)
        next_y = pdf.get_y()
        pdf.multi_cell(w=24, h=2.8, txt=f"{fecha_atencion}")
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_font_size(6)
        pdf.set_xy(pdf.get_x()+30, next_y)
        pdf.cell(w=12, h=6, txt=f"Fecha Cx:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.set_font_size(8)
        pdf.cell(w=24, h=6, txt=f"{fecha_cx}")
        pdf.ln()
        x_start = pdf.get_x() - 6
        x_end = x_start + 72
        y_start = pdf.get_y() + 0.4
        pdf.line(x1=x_start, y1=y_start, x2=x_end, y2=y_start)
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_xy(pdf.get_x()-6, y_start)
        pdf.set_font_size(6)
        pdf.cell(w=12, h=6, txt=f"Cliente:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.multi_cell(w=60, h=4, txt=f"{SelectedGuia['cliente']}")
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.cell(w=12, h=6, txt=f"Entrega:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.multi_cell(w=60, h=4, txt=f"{SelectedGuia['entrega']}")
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.cell(w=12, h=6, txt=f"Paciente:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.cell(w=60, h=6, txt=f"{SelectedGuia['paciente']}")
        pdf.ln()
        x_start = pdf.get_x() - 6
        x_end = x_start + 72
        y_start = pdf.get_y()
        pdf.line(x1=x_start, y1=y_start, x2=x_end, y2=y_start)
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.cell(w=12, h=6, txt=f"Represent.:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.cell(w=60, h=6, txt=f"{SelectedGuia['representante']}")
        pdf.ln()
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.cell(w=12, h=6, txt=f"OC:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.cell(w=24, h=6, txt=f"{SelectedRecord['oc_cliente']}")
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.cell(w=12, h=6, txt=f"NP:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.cell(w=24, h=6, txt=f"{SelectedRecord['nro_proceso']}")
        pdf.ln()
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.cell(w=12, h=6, txt=f"Tipo Guía:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.cell(w=60, h=6, txt=f"{SelectedRecord['tipo_venta']}")
        pdf.ln()
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.cell(w=12, h=6, txt=f"OBS:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.set_font_size(8)
        pdf.multi_cell(w=60, h=8, txt=f"{SelectedGuia['obs']}")
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.set_font_size(6)
        pdf.cell(w=12, h=6, txt=f"Atención:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.set_font_size(8)
        pdf.cell(w=24, h=6, txt=f"{SelectedRecord['atencion']}")
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_font_size(6)
        pdf.cell(w=12, h=6, txt=f"Picking:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.set_font_size(8)
        pdf.multi_cell(w=24, h=6, txt=f"{SelectedRecord['almacen']}")
        pdf.set_font_size(6)
        if SelectedGuia['kits_guia'] is not None and SelectedGuia['kits_guia'] != '':
            kits = SelectedGuia['kits_guia'].split("//")
            print("save_PDF:", kits)
            pdf.set_x(pdf.get_x()-6)
            # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
            pdf.cell(w=12, h=6, txt=f"KIT", align="C", border=1)
            pdf.cell(w=48, h=6, txt=f"DESCRIPCION", align="C", border=1)
            pdf.cell(w=12, h=6, txt=f"CANT.", align="C", border=1)
            pdf.ln()
            nro = 0
            # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
            for row in kits:
                count = 0
                for cel in SelectedDescripcion:
                    if cel['kits_items'] != "" and cel['kits_items'] in row:
                        count = count + 1
                fix = 6
                print('save_PDF:', len(row))
                if len(row) > 36:
                    fix = int(len(row)/36 + 1) * fix
                pdf.set_x(pdf.get_x()-6)
                pdf.cell(w=12, h=fix, txt=str(nro + 1), align="C", border=1)
                next_y = pdf.get_y()
                pdf.multi_cell(w=48, h=6, txt=row, align="C", border=1)
                pdf.set_xy(pdf.get_x()+54, next_y)
                pdf.cell(w=12, h=fix, txt=str(count), align="C", border=1)
                pdf.ln()
                nro = nro + 1
        x_start = pdf.get_x() - 6
        x_end = x_start + 72
        y_start = pdf.get_y()
        pdf.line(x1=x_start, y1=y_start, x2=x_end, y2=y_start)
        # pdf.set_text_color(r=21, g=62, b=194) # Blue Intense in rgb
        pdf.set_x(pdf.get_x()-6)
        pdf.set_font_size(8)
        pdf.cell(w=60, h=8, txt=f"TOTAL DE DOCUMENTO:")
        # pdf.set_text_color(r=20, g=20, b=20) # soft Black in rgb
        pdf.cell(w=12, h=8, txt=f"{sumCantidad}", align="C")
        pdf.ln()
        x_start = pdf.get_x() - 6
        x_end = x_start + 72
        y_start = pdf.get_y()
        pdf.line(x1=x_start, y1=y_start, x2=x_end, y2=y_start)
        x_start = pdf.get_x() + 20
        y_start = pdf.get_y() + 10
        qr = f"http://api.qrserver.com/v1/create-qr-code/?data={SelectedRecord['nro_guia']}-{empr_id}"
        pdf.image(qr, x_start, y_start, 20, 0, 'PNG')
        pdf.ln()
        pdf.output(filename)
        printer_name = 'XP-80C'
        time.sleep(0.2)
        try:
            # Convertir el PDF a imágenes (una página)
            pages = convert_from_path(filename, 2200)
            img = pages[0]
            img_path = filename[:-3] + 'png'
            img.save(img_path, "PNG")
            # Verificar si la impresora está disponible
            printer = win32print.OpenPrinter(printer_name)
            printer_info = win32print.GetPrinter(printer, 2)
            # Abrir el contexto de la impresora
            hdc = win32ui.CreateDC()
            hdc.CreatePrinterDC(printer_name)
            hdc.StartDoc(filename)
            hdc.StartPage()
            # Cargar la imagen guardada
            img = Image.open(img_path)
            # Dibujar la imagen en la impresora
            dib = ImageWin.Dib(img)
            dib.draw(hdc.GetHandleOutput(), (0, 0, 580, 1400))
            # Terminar la pagina, cerrar el archivo y eliminar el contexto
            hdc.EndPage()
            hdc.EndDoc()    
            hdc.DeleteDC()
            # Eliminar la imagen temporal
            os.remove(img_path)
            os.remove(filename)
        except Exception as e:
            return Response({'message': f"Error al enviar a la impresora: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': f'Se imprimió correctamente el ticket: {SelectedRecord['nro_guia']}.'}, status=status.HTTP_200_OK)

class Pend_GuiasViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = Pend_Guias.objects.all().order_by('-id')
    serializer_class = Pend_GuiasSerializer
    permission_classes = get_permissions

class Pend_ItemsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    queryset = Pend_Items.objects.all().order_by('-id')
    serializer_class = Pend_ItemsSerializer
    permission_classes = get_permissions

class RecordSuggestionView(APIView):
    def post(self, request):
        # Obtén el prompt enviado en el cuerpo de la solicitud
        prompt = request.data.get("prompt", "")
        if not prompt:
            return Response({"message": "El prompt no puede estar vacío."}, status=status.HTTP_400_BAD_REQUEST)
        # Genera la sugerencia usando el modelo ONNX
        try:
            suggestion = generate_suggestion(prompt)
            return Response({"message": suggestion}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
