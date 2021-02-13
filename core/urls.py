from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('registrar/', registrar, name='registrar')
]