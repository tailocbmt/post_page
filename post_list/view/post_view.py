from uuid import UUID

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

from post_list.dto.post_dto import PostDto
from post_list.repository.post_repository import PostRepository

_post_repo_instance = PostRepository()


@api_view(["GET"])
def get_all_posts(request: WSGIRequest):
    try:
        options = _post_repo_instance.create_options(request)
        posts = _post_repo_instance.get_all()
        posts = _post_repo_instance.filter_options(posts, options)

        dto = PostDto.Serializer(posts, many=True).data
        return JsonResponse(dto, safe=False)
    except Exception as e:
        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content=e,
        )


@api_view(["POST"])
def create_post(request: WSGIRequest):
    try:
        request_data = _post_repo_instance.get_request_data(request)
        post = _post_repo_instance.create_post(request_data)

        dto = PostDto.Serializer(post).data
        return JsonResponse(dto, safe=False)
    except Exception as e:
        return HttpResponse(
            status=status.HTTP_400_BAD_REQUEST,
            content=e,
        )
