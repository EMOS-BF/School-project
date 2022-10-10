from django.forms import ModelForm
from .models import Eleve
from django import forms

class EleveForm(ModelForm):
    class Meta:
        model= Eleve
        fields=['INE_eleve' , 'nom_eleve' , 'prenom_eleve' , 'date_de_naissance' , 'filiere' , 'Classe' , 'est_chef']
