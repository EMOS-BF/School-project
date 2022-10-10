from django.contrib import admin
from .models import Eleve
class EleveAdmin(admin.ModelAdmin):
    list_display = ('INE_eleve','nom_eleve','prenom_eleve','date_de_naissance','filiere','Classe','est_chef')
    search_fields = ['nom_eleve','prenom_eleve']
# Register your models here.
admin.site.register(Eleve,EleveAdmin)
