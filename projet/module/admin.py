from django.contrib import admin
from .models import Module
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('Identifiant','nom','nombre_heure','semestre')
    search_fields = ['nom']
# Register your models here.
admin.site.register(Module,ModuleAdmin)