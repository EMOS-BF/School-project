from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_classe(request):
    return HttpResponse("La liste des Module pour une classe donnée")