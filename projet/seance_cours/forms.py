from django.forms import ModelForm
from .models import SeanceCours
from django import forms

class CoursForm(ModelForm):
    class Meta:
        model= SeanceCours
        fields=['Enseignant' , 'nombre_heure' ,'Module']