# daphne_test.py
from django.core.handlers.asgi import ASGIHandler

async def application(scope, receive, send):
    if scope["type"] == "http":
        await ASGIHandler()(scope, receive, send)
    elif scope["type"] == "websocket":
        while True:
            event = await receive()
            if event["type"] == "websocket.connect":
                await send({"type": "websocket.accept"})
            elif event["type"] == "websocket.disconnect":
                break
            elif event["type"] == "websocket.receive":
                await send({
                    "type": "websocket.send",
                    "text": f"Recibido: {event['text']}"
                })