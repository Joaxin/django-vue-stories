from rest_framework import serializers
from ..models import Message
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class MessageSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Message
        fields = ['id', 'author','content','tags','is_public']



