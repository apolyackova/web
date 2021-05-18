from django.urls import path
from .views import *

urlpatterns = [
    path('', first, name='first'),
    path('home/', home, name='home'),
]