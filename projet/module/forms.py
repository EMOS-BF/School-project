from django.forms import ModelForm
from .models import Module
from django import forms

class ModuleForm(ModelForm):
    class Meta:
        model= Module
        fields=['Identifiant' , 'nom' , 'nombre_heure','semestre']
