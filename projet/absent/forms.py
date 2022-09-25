from django.forms import ModelForm
from .models import Absent
from django import forms

class AbsentForm(ModelForm):
    class Meta:
        model= Absent
        fields=['Eleve' , 'Cours' , 'motif']
