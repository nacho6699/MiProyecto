from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from .forms import *
# Create your views here.
def view_principal(request):
	return render_to_response("inicio.html", {},context_instance=RequestContext(request))

def view_registrar(request):
	formularioRegistro=fUsuario()
	return render_to_response("usuario/registrar.html", {"formulario":formularioRegistro},context_instance=RequestContext(request))