from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser
from asgiref.sync import sync_to_async
import logging

logger = logging.getLogger(__name__)

class JWTAuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        scope['user'] = AnonymousUser()
        headers = dict(scope['headers'])
        # logger.debug(f"headers: {str(headers)}")
        # Función síncrona envuelta para uso asíncrono
        @sync_to_async
        def get_user_from_token(token):
            try:
                jwt_auth = JWTAuthentication()
                validated_token = jwt_auth.get_validated_token(token)
                return jwt_auth.get_user(validated_token)
            except Exception as e:
                logger.debug(f"Error get_user_from_token: {str(e)}")
                return AnonymousUser()
        
        if b'authorization' in headers:
            try:
                auth_header = headers[b'authorization'].decode()
                if auth_header.startswith('Bearer '):
                    token = auth_header.split(' ')[1]
                    scope['user'] = await get_user_from_token(token)
            except Exception as e:
                logger.debug(f"Error de autenticación: {str(e)}")
        
        return await self.app(scope, receive, send)