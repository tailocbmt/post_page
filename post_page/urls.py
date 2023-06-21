"""post_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from post_list.view.comment_view import create_comment, get_post_comment
from post_list.view.home_view import home, page
from post_list.view.post_view import create_post, get_all_posts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('page', page, name="page"),
    path('posts/get_all', get_all_posts),
    path('posts/create', create_post),
    path('comments/<str:post_id>/get_all', get_post_comment),
    path('comments/create', create_comment)
]
