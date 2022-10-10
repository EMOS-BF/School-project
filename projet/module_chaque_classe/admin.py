from django.contrib import admin
from .models import ClasseModule
class ClasseModuleAdmin(admin.ModelAdmin):
    list_display = ('Classe','Module')
    search_fields = ['Classe']
# Register your models here.
admin.site.register(ClasseModule,ClasseModuleAdmin)
