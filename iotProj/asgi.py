import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from mqtt_topics.consumers import MyMqttConsumer
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
import iotApp.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iotProj.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'mqtt': MyMqttConsumer.as_asgi(),
    'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(iotApp.routing.websocket_urlpatterns)))
})
