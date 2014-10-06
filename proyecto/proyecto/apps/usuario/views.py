from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
# Create your views here.
def view_principal(request):
	return render_to_response("inicio.html", {},context_instance=RequestContext(request))

def view_registrar(request):
	return render_to_response("usuario/registrar.html", {},context_instance=RequestContext(request))