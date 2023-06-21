from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def home(request: WSGIRequest):
    return render(request, 'index.html')


def page(request: WSGIRequest):
    return render(request, 'page.html')
