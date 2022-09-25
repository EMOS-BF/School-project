from django.contrib import admin
from .models import Absent
class AbsentAdmin(admin.ModelAdmin):
    list_display = ('Eleve','Cours','motif')
    search_fields = ['Eleve']
# Register your models here.
admin.site.register(Absent,AbsentAdmin)