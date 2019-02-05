from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Publicacion
from .models import Detalle


# Create your views here.


def publicacion_detalle(request, id=None):
    instance = Publicacion.objects.get(id=id)
    queryset = Detalle.objects.filter(publicacion_id=id)
    context = {
        "object_list": queryset,
        "instance":instance,
    }
    return render(request, "detalle_publicacion.html", context)


def base(request):
    queryset = Publicacion.objects.all()
    context = {
        "titulo": "listado",
        "object_list": queryset,
    }
    return render(request, "index.html", context)
