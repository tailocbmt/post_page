from typing import Dict

from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet

from post_list.models import Post
from post_list.repository.base_repository import BaseRepository


class PostRepository(BaseRepository):
    def get_all(self) -> QuerySet:
        try:
            posts = Post.objects.all()

            return posts
        except Exception as e:
            raise BadRequest(
                f"Cannot get all post: {e}"
            )

    def create_post(self, data: Dict):
        try:
            post = Post(**data)
            post.save()

            return post
        except Exception as e:
            raise BadRequest(
                f"Cannot create post: {e}"
            )
