from django.urls import path
from . import views

urlpatterns = [
    path('Asist_Virtual/', views.Asist_Virtual),
] #+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)