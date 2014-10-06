#encoding:utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class fperfil(ModelForm):
	class Meta:
		model=Perfil
		exclude=['user']

class fUsuario(UserCreationForm):
	username=forms.CharField(max_length=50,required=True,help_text=False,label="Nick:")
	password2=forms.CharField(help_text=False,label="Confirmar pasword:",widget=forms.PasswordInput)
	email=forms.EmailField(max_length=50,required=True,label="Email:")

class Meta:
	model=User
	fields=("username","password1","password2","email")
def save(self, commit=True):
	user=super(fUsuario.self).save(commit=False)
	user.email=self.cleaned_data.get("email")
	if commit:
		user.save()
	return user