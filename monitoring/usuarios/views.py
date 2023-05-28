from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, Http404
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse
import json
from .models import Usuario

def UsuarioList(request):
    queryset = Usuario.objects.all()
    context = list(queryset.values('id', 'nombre'))
    return JsonResponse(context, safe=False)

def UsuarioDetail(request, id):
    try:
        usuario = Usuario.objects.get(id=id)
        context = {'id': usuario.id, 'nombre': usuario.nombre}
        return JsonResponse(context)
    except Usuario.DoesNotExist:
        raise Http404

def UsuarioCreate(request):
    if request.method == 'POST':
        data=request.body.decode('utf-8')
        data_json = json.loads(data)
        usuario = Usuario()
        usuario.nombre = data_json["nombre"]
        usuario.profesion = data_json["profesion"]
        usuario.eps = data_json["eps"]
        usuario.save()
        return HttpResponse("successfully created variable")
