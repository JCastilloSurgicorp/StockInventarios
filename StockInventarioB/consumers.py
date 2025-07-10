# tu_app/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class MiConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
    
    async def disconnect(self, close_code):
        pass
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        # Lógica de negocio (ej: guardar en BD, enviar a otro cliente)
        await self.send(text_data=json.dumps({"respuesta": "Mensaje recibido"}))