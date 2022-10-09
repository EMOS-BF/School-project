from django.shortcuts import render,redirect
from eleve.models import Eleve
from absent.models import Absent
from .filters import EleveFiltre
from .forms import EleveForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
#from compte.decorators import allowed_users
# Create your views here.
from .models import *
@login_required(login_url='acces')
#@allowed_users(allowed_roles=['Admin'])
def home(request):
    Eleves=Eleve.objects.all()
    context = {'Eleves':Eleves}
    if request.user.groups.filter(name='Eleve').exists() or request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionAbsencesCours').exists() or request.user.groups.filter(name='Supervision').exists() :
        return render(request, 'eleve/acceuil.html',context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')


@login_required(login_url='acces')
#@allowed_users(allowed_roles=['Admin'])
def gestionIndividuel(request,pk):
    eleve = Eleve.objects.get(INE_eleve=pk)
    absent = eleve.absent_set.all()
    Absence_total=absent.count()
    myFilter=EleveFiltre(request.GET,queryset=absent)
    absent=myFilter.qs
    context = {'Eleve': eleve,'absent':absent,'Absence_total':Absence_total,'myFilter':myFilter}
    if request.user.groups.filter(name='Eleve').exists() or request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionEleve').exists():
        return render(request, 'eleve/gestionIdividuel.html',context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')


@login_required(login_url='acces')
#@allowed_users(allowed_roles=['Admin'])
def Ajouter_eleve(request):
    form=EleveForm()
    if request.method=='POST':
        form=EleveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionEleve').exists():
        return render(request, 'eleve/ajouter_eleve.html',context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')


@login_required(login_url='acces')
#@allowed_users(allowed_roles=['Admin'])
def modifier_eleve(request,pk):
    eleve=Eleve.objects.get(INE_eleve=pk)
    form = EleveForm(instance=eleve)
    if request.method == 'POST':
        form = EleveForm(request.POST,instance=eleve)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionEleve').exists():
        return render(request, 'eleve/ajouter_eleve.html', context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')


@login_required(login_url='acces')
#@allowed_users(allowed_roles=['Admin'])
def supprimer_eleve(request,pk):
    eleve = Eleve.objects.get(INE_eleve=pk)
    if request.method == 'POST':
        eleve.delete()
        return redirect('/')
    context={'item':eleve}
    if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionEleve').exists():
        return render(request, 'eleve/supprimer_eleve.html',context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')

