from django.contrib import admin
from .models import SeanceCours
class SeanceCoursAdmin(admin.ModelAdmin):
    list_display = ('Enseignant','nombre_heure','date','Module')
    search_fields = ['Module']
# Register your models here.
admin.site.register(SeanceCours,SeanceCoursAdmin)