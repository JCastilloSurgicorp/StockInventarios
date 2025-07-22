"""
ASGI config for DjangoSQLrestAPI project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoSQLrestAPI.settings')
django.setup()

from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
from StockInventarioB.middleware import JWTAuthMiddleware
from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
from StockInventarioB import routing

# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # HTTP (DRF)
    # "websocket": get_asgi_application(),
    "websocket": AllowedHostsOriginValidator(
        JWTAuthMiddleware(
            URLRouter(
                routing.websocket_urlpatterns  # Rutas para WebSockets
            )
        )
    ),
})
