from datetime import datetime

from rest_framework import serializers


class CommentDto():
    id: str
    created_datetime: datetime

    post_id: str
    author_name: str
    content: str

    class Serializer(serializers.Serializer):
        id = serializers.UUIDField(read_only=True)
        created_datetime = serializers.DateTimeField(read_only=True)

        post_id = serializers.UUIDField()
        author_name = serializers.CharField()
        content = serializers.CharField()
