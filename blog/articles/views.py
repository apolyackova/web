from django.http import HttpResponse
from django.shortcuts import render

from .models import *


def archive(request):
    context = {"posts": Article.objects.all()}
    return render(request, 'archive.html', context=context)
