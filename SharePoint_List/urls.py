from django.urls import path
from .views import *

urlpatterns = [
    path('lists/<str:list_title>/', SharePointListView.as_view()),
    path('lists/<str:list_title>/items/<str:item_id>/', SharePointItemDetailView.as_view()),
]