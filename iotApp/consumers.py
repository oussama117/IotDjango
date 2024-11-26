import json
from channels.generic.websocket import AsyncWebsocketConsumer


class SensorDataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()
        await self.send(text_data=json.dumps({'msg': 'Connected to WebSocket server'}))
        self.room_group_name = "send_sensor_data"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        print(f"WebSocket connected and added to group '{self.room_group_name}'")


    async def send_sensor_data(self, event):
        # Extract and send the payload from the event
        try:
            message = event["payload"]
            await self.send(text_data=json.dumps(message))
        except KeyError as e:
            print(f"KeyError: {e} - Event: {event}")
            await self.send(text_data=json.dumps({'error': 'Invalid data received'}))

    async def disconnect(self, close_code):
        # Remove the WebSocket connection from the group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
        print(f"WebSocket disconnected from group '{self.room_group_name}'")
