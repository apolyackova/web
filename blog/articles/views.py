from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import *


def archive(request):
    context = {"posts": Article.objects.all()}
    return render(request, 'archive.html', context=context)


def article(request, id):
    try:
        article = Article.objects.get(id=id)
        return render(request, 'article.html', context={'post': article})
    except:
        return Http404()


def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect(reverse('/'))

    if request.method == "GET":
        form = ArticleForm()
        return render(request, 'add_article.html', context={'form': form})

    return HttpResponse(status=403)

