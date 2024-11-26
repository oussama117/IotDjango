from django.urls import re_path
from iotApp import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/',consumers.SensorDataConsumer.as_asgi())
]