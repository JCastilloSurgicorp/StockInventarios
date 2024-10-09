from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Asist_Virtual/', views.Asist_Virtual)
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)