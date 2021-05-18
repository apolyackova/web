from django.http import HttpResponse
from django.shortcuts import render


def first(request):
    return HttpResponse('Привет, Мир!')


def home(request):
    return render(request, template_name='templates/home.html')
