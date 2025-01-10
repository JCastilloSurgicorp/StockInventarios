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
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt import views as jwt_views
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from django.urls import path, include
from SI_Flet.views import SI_Flet
from django.conf import settings
from django.contrib import admin


urlpatterns = [
    path('', include('StockInventarioB.urls')),
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='SI Api Documentation')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('SI_Flet.urls')),
    path('', include('AsistVirtual.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + debug_toolbar_urls()