from uuid import UUID

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from post_list.dto.comment_dto import CommentDto
from post_list.repository.comment_repository import CommentRepository

_comment_repo_instance = CommentRepository()


@api_view(["GET"])
def get_post_comment(request: WSGIRequest, post_id: UUID):
    try:
        post_id = UUID(post_id)
        options = _comment_repo_instance.create_options(request)
        post = _comment_repo_instance.check_exist(post_id)

        comments = _comment_repo_instance.get_post_comments(post)
        comments = _comment_repo_instance.filter_options(comments, options)

        dto = CommentDto.Serializer(comments, many=True).data
        return JsonResponse(dto, safe=False)
    except Exception as e:
        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content=e,
        )


@api_view(["POST"])
def create_comment(request: WSGIRequest):
    try:
        request_data = _comment_repo_instance.get_request_data(request)
        _comment_repo_instance.check_exist(request_data["post_id"])
        comment = _comment_repo_instance.create_comment(request_data)

        dto = CommentDto.Serializer(comment).data
        return JsonResponse(dto, safe=False)
    except Exception as e:
        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content=e,
        )
