import uuid
from datetime import datetime

from django.db import models


# Create your models here.
class Post(models.Model):
    class Meta:
        app_label = "post_list"
        db_table = "post"

    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, max_length=36, primary_key=True)
    created_datetime = models.DateTimeField(default=datetime.now, blank=True)

    title = models.CharField(max_length=256, blank=False)
    author_name = models.CharField(max_length=120, blank=False)
    content = models.TextField(blank=False)


class Comment(models.Model):
    class Meta:
        app_label = "post_list"
        db_table = "comment"

    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          unique=True, max_length=36, primary_key=True)
    created_datetime = models.DateTimeField(default=datetime.now, blank=True)
    post = models.ForeignKey(
        Post, max_length=36, on_delete=models.CASCADE, db_column="post_id"
    )

    author_name = models.CharField(max_length=128, blank=False)
    content = models.TextField(blank=False)
