from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import HojaPicking 
import logging

logger = logging.getLogger(__name__)

@receiver([post_save, post_delete], sender=HojaPicking)
def notificar_cambio_hoja_picking(sender, instance, **kwargs):
    try:
        action = "actualizada" if 'created' in kwargs and not kwargs['created'] else "creada"
        if kwargs.get('signal') == post_delete:
            action = "eliminada"
        logger.debug(f"{action}: HojaPicking({sender}) -> {instance}")
        # Enviar notificación a todos los clientes
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notificaciones_global",
            {
                "type": "notificacion.sistema",
                "message": f"Hoja de Picking {action}: {instance}"
            }
        )
    except Exception as e:
        logger.debug(f"ERROR notificar_cambio: {str(e)}")