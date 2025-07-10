# tu_app/routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/ruta/", consumers.MiConsumer.as_asgi()),
]