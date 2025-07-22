# tu_app/routing.py
from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path("ws/test", EchoConsumer.as_asgi()),
    # path("ws/ruta/", MiConsumer.as_asgi()),
    path('ws/notificaciones', NotificacionesConsumer.as_asgi()),
]