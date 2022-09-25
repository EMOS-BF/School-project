from django.shortcuts import render,redirect
from .models import Absent
from .forms import AbsentForm
from .filters import AbsentFiltre
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='acces')
def list_absent(request):
    absent=Absent.objects.all()
    myFilter = AbsentFiltre(request.GET, queryset=absent)
    absent = myFilter.qs
    context={'Absents':absent,'myFilter': myFilter}
    return render(request, 'absent/list_absent.html',context)

"""def recherche(request):
    absent = Absent.objects.all()
    myFilter = AbsentFiltre(request.GET, queryset=absent)
    absent = myFilter.qs
    context = { 'absent': absent, 'myFilter': myFilter}
    return render(request, 'list_absent.html',context)"""

@login_required(login_url='acces')
def Ajouter_absent(request):
    form=AbsentForm()
    if request.method=='POST':
        form=AbsentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('absent')
    context={'form':form}
    return render(request, 'absent/ajouter_absent.html',context)

@login_required(login_url='acces')
def modifier_absent(request,pk):
    absent=Absent.objects.get(id=pk)
    form = AbsentForm(instance=absent)
    if request.method == 'POST':
        form = AbsentForm(request.POST,instance=absent)
        if form.is_valid():
            form.save()
            return redirect('absent')
    context = {'form': form}
    return render(request, 'absent/ajouter_absent.html', context)


@login_required(login_url='acces')
def supprimer_absent(request,pk):
    absent = Absent.objects.get(id=pk)
    if request.method == 'POST':
        absent.delete()
        return redirect('absent')
    context={'item':absent}
    return render(request, 'absent/supprimer_absent.html',context)