from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from django.db.models.signals import post_save
from asgiref.sync import async_to_sync
from django.dispatch import receiver
from django.conf import settings
from .models import *
import logging
import json

logger = logging.getLogger(__name__)

class EchoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        
    async def receive(self, text_data):
        await self.send(text_data=f"Recibido: {text_data}")

class NotificacionesConsumer(AsyncWebsocketConsumer):
    GROUP_NAME = 'notificaciones_global'

    async def connect(self):
        try:
            user = self.scope.get("user", AnonymousUser())
            logger.debug(f"Conectado: Usuario->{user.username} ({self.channel_name})")
            # Aceptar conexión
            await self.accept()
            # Unirse al grupo global
            await self.channel_layer.group_add(
                self.GROUP_NAME,
                self.channel_name
            )
            # Enviar confirmación
            await self.send(text_data=json.dumps({
                'type': 'connection_established',
                'message': 'Conectado correctamente a Notificaciones Globales'
            }))
            # Enviar mensaje de prueba al unirse
            await self.channel_layer.group_send(
                "notificaciones_global",
                {
                    "type": "notificacion.sistema",
                    "message": f"Conectado: Usuario->{user.username}"
                }
            )
        except Exception as e:
            logger.debug(f"ERROR - connect: {str(e)}")
            await self.close(code=1011) 
        
    async def disconnect(self, close_code):
        logger.debug(f"Desconexión con código: {close_code}")
        # Abandonar grupo al desconectarse
        await self.channel_layer.group_discard(
            self.GROUP_NAME,
            self.channel_name
        )

    # Recibir mensajes del cliente
    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            usuario = self.get_username()
            # Lógica para manejar mensajes entrantes
            await self.channel_layer.group_send(
                self.GROUP_NAME,
                {
                    'type': 'broadcast_message',
                    'message': data['message'],
                    'sender': usuario
                }
            )
        except Exception as e:
            logger.debug(f"ERROR - receive: {str(e)}")
            await self.send(text_data=json.dumps({
                'type': 'error',
                'message': f'Error: {str(e)}'
            }))

    async def notificacion_sistema(self, event):
        """Maneja notificaciones del sistema"""
        try:
            logger.debug(f"system_notification: sistema -> {event['message']}")
            await self.send(text_data=json.dumps({
                'type': 'system_notification',
                'message': event['message'],
                'sender': 'sistema'
            }))
        except Exception as e:
            logger.debug(f"ERROR - notificacion_sistema: {str(e)}")

    async def broadcast_message(self, event):
        """Maneja mensajes de broadcast de usuarios"""
        try:
            # logger.debug(f"broadcast_message: {event.get('sender')} -> {event['message']}")
            await self.send(text_data=json.dumps({
                'type': 'broadcast',
                'message': event['message'],
                'sender': event['sender']
            }))
        except Exception as e:
            logger.debug(f"ERROR - broadcast_message: {str(e)}")

    # Función para obtener el nombre de usuario
    def get_username(self):
        user = self.scope["user"]
        if user.is_authenticated:
            return user.username
        return "No Autenticado"

# Señal para notificar cambios en modelos
@receiver(post_save, sender=HojaPicking)
def notificar_cambio(sender, instance, created, **kwargs):
    from asgiref.sync import async_to_sync
    from channels.layers import get_channel_layer

    try:
        channel_layer = get_channel_layer()
        
        async_to_sync(channel_layer.group_send)(
            NotificacionesConsumer.GROUP_NAME,
            {
                "type": "broadcast_message",
                "message": {
                    "event": "actualizacion",
                    "model": sender.__name__,
                    "id": instance.id
                }
            }
        )
    except Exception as e:
        logger.debug(f"ERROR - notificar_cambio: {str(e)}")

class MiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.channel_name)
        self.GROUP_NAME = 'notificacions'
        async_to_sync(self.channel_layer.group_add)(
            self.GROUP_NAME, self.channel_name
        )
        self.accept()
    
    async def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.GROUP_NAME, self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        # Lógica de negocio (ej: guardar en BD, enviar a otro cliente)
        await self.send(text_data=json.dumps({"respuesta": "Mensaje recibido"}))

# class AzureSignalRConsumer:
#     async def connect(self):
#         self.connection_string = settings.AZURE_SIGNALR_CONNECTION_STRING
#         # Extraer datos de la cadena de conexión
#         endpoint = self.connection_string.split(";")[0].split("=")[1]
#         access_key = self.connection_string.split(";")[1].split("=")[1]
        
#         self.websocket = await websockets.connect(
#             f"wss://{endpoint}/client/hubs/hubname",
#             extra_headers={"Authorization": f"Bearer {self.generate_jwt(access_key, endpoint)}"}
#         )

#     def generate_jwt(self, access_key, audience):
#         import jwt
#         import time
#         payload = {
#             "aud": audience,
#             "exp": int(time.time()) + 3600  # 1 hora de validez
#         }
#         return jwt.encode(payload, access_key, algorithm="HS256")

#     async def receive(self, text_data):
#         await self.websocket.send(text_data)
#         response = await self.websocket.recv()
#         return response