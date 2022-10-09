from django.shortcuts import render,redirect
from .models import Module
from .forms import ModuleForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

@login_required(login_url='acces')
def list_module(request):
    Modules = Module.objects.all()
    context = {'Modules': Modules}
    if request.user.groups.filter(name='Supervision').exists() or request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionModule').exists():
        return render(request,'module/list_module.html',context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')

@login_required(login_url='acces')
def Ajouter_module(request):
    form=ModuleForm()
    if request.method=='POST':
        form=ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module')
    context={'form':form}
    if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionModule').exists():
        return render(request, 'module/ajouter_module.html',context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')

@login_required(login_url='acces')
def modifier_module(request,pk):
    module=Module.objects.get(id=pk)
    form = ModuleForm(instance=module)
    if request.method == 'POST':
        form = ModuleForm(request.POST,instance=module)
        if form.is_valid():
            form.save()
            return redirect('module')
    context = {'form': form}
    if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionModule').exists():
        return render(request, 'module/ajouter_module.html', context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')

@login_required(login_url='acces')
def supprimer_module(request,pk):
    module = Module.objects.get(id=pk)
    if request.method == 'POST':
        module.delete()
        return redirect('module')
    context={'item':module}
    if request.user.groups.filter(name='Admin').exists() or request.user.groups.filter(name='GestionModule').exists():
        return render(request, 'module/supprimer_module.html',context)
    else:
        return HttpResponse('<h1>Vous n\'est pas autorisé à voir ce contenu</h1>')