"""
ASGI config for DjangoSQLrestAPI project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from StockInventarioB import routing
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSQLrestAPI.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP (DRF)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns  # Rutas para WebSockets
        )
    ),
})
