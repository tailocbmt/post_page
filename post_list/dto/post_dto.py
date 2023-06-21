from datetime import datetime

from rest_framework import serializers


class PostDto():
    id: str
    created_datetime: datetime

    title: str
    author_name: str
    content: str

    class Serializer(serializers.Serializer):
        id = serializers.UUIDField(read_only=True)
        created_datetime = serializers.DateTimeField(read_only=True)

        title = serializers.CharField()
        author_name = serializers.CharField()
        content = serializers.CharField()
