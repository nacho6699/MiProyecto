from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.models import User
from .forms import *
from .models import *
# Create your views here.
def view_principal(request):
	return render_to_response("inicio.html", {},context_instance=RequestContext(request))

def view_registrar(request):
	if request.method=="POST":
		formularioRegistro=fUsuario(request.POST)
		if formularioRegistro.is_valid():
			nuevo_usuario=request.POST['username']
			formularioRegistro.save()
			usuario=User.objects.get(username=nuevo_usuario)
			usuario.is_active=False
			usuario.save()
			perfil=Perfil.objects.create(user=usuario)
			return HttpResponse("Registrado")
	else:
		formularioRegistro=fUsuario()
	return render_to_response("usuario/registrar.html",{'formulario':formularioRegistro},context_instance=RequestContext(request))
