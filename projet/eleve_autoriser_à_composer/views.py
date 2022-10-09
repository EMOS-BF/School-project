from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def list_eleve_autoriser_à_composer(request):
    if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionAbsencesCours').exists() or request.user.groups.filter(name='Supervision').exists():
        return render(request,'eleve_autoriser_à_composer/list_eleve_autoriser_à_composer.html')
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')
