from .models import ParkInfo
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=ParkInfo)
def db_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "updates_group",
        {
            "type": "space_update",
            "slot_status": instance.slot_status,
        },
    )
