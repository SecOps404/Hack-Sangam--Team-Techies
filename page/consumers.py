import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AppConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("updates_group", self.channel_name)

    async def disconnect(self, close_code):
        print("connection closed with code: {}", close_code)
        await self.channel_layer.group_discard("updates_group", self.channel_name)

    async def space_update(self, event):
        slot_status = event['slot_status']
        await self.send(text_data=json.dumps({
            'slot_status': slot_status,
        }))
