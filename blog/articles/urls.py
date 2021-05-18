from django.urls import path

from .views import *


urlpatterns = [
    path('', archive),
    path('article/<int:id>/', article,)
]