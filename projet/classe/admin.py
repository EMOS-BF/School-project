from django.contrib import admin
from .models import Classe
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('nom','id')
    search_fields = ['nom']
# Register your models here.
admin.site.register(Classe,ClasseAdmin)