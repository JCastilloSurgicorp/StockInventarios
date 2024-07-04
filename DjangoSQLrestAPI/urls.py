"""
URL configuration for DjangoSQLrestAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from rest_framework.documentation import include_docs_urls
from StockInventarioB import views


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

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='SI Api Documentation')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + debug_toolbar_urls()
