from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'linea', views.SI_LineaViewSet)
router.register(r'Grupo', views.SI_GrupoViewSet)
router.register(r'Productos', views.SI_ProductosViewSet)
router.register(r'TipoProductos', views.SI_TipoProductosViewSet)
router.register(r'Empresa', views.SI_EmpresaViewSet)
router.register(r'Depositos', views.SI_DepositosViewSet)
router.register(r'TipoAlmacen', views.SI_TipoAlmacenViewSet)
router.register(r'Sector', views.SI_SectorViewSet)
router.register(r'StocksInventario', views.StocksInventarioViewSet)
router.register(r'GuiasRemision', views.GuiasRemisionViewSet)
router.register(r'GR_Descripcion', views.GR_DescripcionViewSet)
router.register(r'GuiasRemision_OC', views.GuiasRemision_OCViewSet)
router.register(r'GR_Descripcion_OC', views.GR_Descripcion_OCViewSet)
router.register(r'GR_Busqueda', views.GR_BusquedaViewSet)
router.register(r'Fact_Busqueda', views.Fact_BusquedaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('question/', views.Question)
]