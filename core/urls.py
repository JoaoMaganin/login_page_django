from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('login/', logar, name='login'),
    path('registrar/', registrar, name='registrar'),
    path('logout/', logout, name='logout')
]
