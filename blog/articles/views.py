from django.http import Http404
from django.shortcuts import render

from .models import *


def archive(request):
    context = {"posts": Article.objects.all()}
    return render(request, 'archive.html', context=context)


def article(request, id):
    try:
        article = Article.objects.get(id=id)
        return render(request, 'article.html', context={'post': article})
    except:
        return Http404

