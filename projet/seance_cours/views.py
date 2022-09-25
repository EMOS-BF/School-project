from django.shortcuts import render,redirect
from .models import SeanceCours
from .forms import CoursForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.
def list_cours(request):
    Cours=SeanceCours.objects.all()
    context={'Cours':Cours}
    return render(request,'seance_cours/list_cours.html',context)

@login_required(login_url='acces')
def Ajouter_cours(request):
    form=CoursForm()
    if request.method=='POST':
        form=CoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cours')
    context={'form':form}
    return render(request, 'seance_cours/ajouter_cours.html',context)

@login_required(login_url='acces')
def modifier_cours(request,pk):
    cours=SeanceCours.objects.get(id=pk)
    form = CoursForm(instance=cours)
    if request.method == 'POST':
        form = CoursForm(request.POST,instance=cours)
        if form.is_valid():
            form.save()
            return redirect('cours')
    context = {'form': form}
    return render(request, 'seance_cours/ajouter_cours.html', context)

@login_required(login_url='acces')
def supprimer_cours(request,pk):
    cours = SeanceCours.objects.get(id=pk)
    if request.method == 'POST':
        cours.delete()
        return redirect('cours')
    context={'item':cours}
    return render(request, 'seance_cours/supprimer_cours.html',context)