from django.contrib import admin
from .models import Eleve_autoriser_composer
class Eleve_autoriser_composerAdmin(admin.ModelAdmin):
    list_display = ('Eleve','Module')
    search_fields = ['Eleve']
# Register your models here.
admin.site.register(Eleve_autoriser_composer,Eleve_autoriser_composerAdmin)