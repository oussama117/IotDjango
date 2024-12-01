import json
from mqttasgi.consumers import MqttConsumer
from db_connection import collection

class MyMqttConsumer(MqttConsumer):
    async def connect(self):
        await self.subscribe('sensors/data', 2)
        print("Subscribed to 'sensors/data'")
        self.room_group_name = "send_sensor_data"
        # await self.channel_layer.group_add(
        #     self.room_group_name,
        #     self.channel_name,
        # )
        print("Added to room_group 'send_sensor_data'")

    async def receive(self, mqtt_message):
        print('Received a message at topic:', mqtt_message['topic'])
        print('With payload', mqtt_message['payload'])
        print('And QOS:', mqtt_message['qos'])
        data = json.loads(mqtt_message['payload'])

        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         "type": "send_sensor_data",
        #         "payload": data
        #     },
        # )
        print("Forwarded data to WebSocket group")

        # Save to MongoDB
        new_data_point = {
            'time': data['time'],
            'acc': data['acc'],
            'gyr': data['gyr'],
            'pulse': data['pulse'],
            'temp': data['temp']
        }
        result = collection.update_one(
            {'idNecklace': data['idNecklace']},  # Find the document by idNecklace
            {'$push': {'data': new_data_point}}  # Push new_data to the 'data' array
        )

        if result.matched_count == 0:
            # If no document was found, create a new one
            collection.insert_one({
                'idNecklace': data['idNecklace'],
                'data': [new_data_point]
            })
        res = collection.find_one({'idNecklace':data['idNecklace']})
        print(f"inserted data into MongoDB: {res}")
    
    async def send_sensor_data(self, event):
        message = event["payload"]
        await self.send_json(message)  # Send to WebSocket or handle appropriately


    async def disconnect(self, code):
            await self.unsubscribe('sensors/data')
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
            print(f"Disconnected and unsubscribed from 'sensors/data'")
            pass
    
        
