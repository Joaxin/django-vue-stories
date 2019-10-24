from rest_framework import generics
from ..models import Message
from .serializers import MessageSerializer
from rest_framework import viewsets

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.filter(is_public=True)
    serializer_class = MessageSerializer

from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

class MessageView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)