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
    return render(request,'module/list_module.html',context)

@login_required(login_url='acces')
def Ajouter_module(request):
    form=ModuleForm()
    if request.method=='POST':
        form=ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('module')
    context={'form':form}
    return render(request, 'module/ajouter_module.html',context)

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
    return render(request, 'module/ajouter_module.html', context)

@login_required(login_url='acces')
def supprimer_module(request,pk):
    module = Module.objects.get(id=pk)
    if request.method == 'POST':
        module.delete()
        return redirect('module')
    context={'item':module}
    return render(request, 'module/supprimer_module.html',context)