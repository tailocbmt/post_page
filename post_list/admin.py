from django.contrib import admin

# Register your models here.
from post_list.models import Comment, Post

admin.site.register(Post)
admin.site.register(Comment)
