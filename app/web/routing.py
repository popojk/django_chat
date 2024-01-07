from django.urls import path, include
from web.consumers import ChatConsumer

websocket_urlpatterns = [
  path("", ChatConsumer.as_asgi()),
]