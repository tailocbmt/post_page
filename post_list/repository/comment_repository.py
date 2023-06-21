from typing import Dict
from uuid import UUID

from django.core.exceptions import BadRequest
from django.db.models.query import QuerySet

from post_list.models import Comment, Post
from post_list.repository.base_repository import BaseRepository


class CommentRepository(BaseRepository):
    def check_exist(self, post_id: UUID):
        post = Post.objects.filter(id=post_id)

        if not post.exists():
            raise BadRequest(
                f"Post with id {post_id} does not exist"
            )
        return post.first()

    def get_post_comments(self, post: Post) -> QuerySet:
        try:
            comments = Comment.objects.filter(
                post_id=post
            )

            return comments
        except Exception as e:
            raise BadRequest(
                f"Cannot get comment of post {post.id}: {e}"
            )

    def create_comment(self, data: Dict):
        try:
            comment = Comment(**data)
            comment.save()

            return comment
        except Exception as e:
            raise BadRequest(
                f"Cannot create comment of post id {data['post_id']}: {e}"
            )
