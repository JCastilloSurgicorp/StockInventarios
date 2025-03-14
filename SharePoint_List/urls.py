from django.urls import path
from . import views

urlpatterns = [
    path('Sharepoint_List/', views.SharePoint_List)
]