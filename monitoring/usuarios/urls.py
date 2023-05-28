from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^usuarios/', views.UsuarioList, name='usuarioList'),
    path('usuarios/<int:id>/', views.UsuarioDetail, name='usuarioDetail'),
    url(r'^usuariocreate/$', csrf_exempt(views.UsuarioCreate), name='usuarioCreate'),
]