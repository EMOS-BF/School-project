from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from .forms import CreerUtilisateur
#from .decorators import utilisateurNonAuthentifier
# Create your views here.
#@utilisateurNonAuthentifier
def incriptionPage(request):
    form = CreerUtilisateur()
    if request.method== 'POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'compte créer avec succès pour ' + user)
            return redirect('acces')
    context={'form':form}
    return render(request,'compte/incription.html',context)

#@utilisateurNonAuthentifier
def accesPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('acceuil:acceuil')
        else:
            messages.info(request,"il y'a une erreur dans le nom d'utilisateur ou le mot de passe")
    return render(request,'compte/acces.html')

def logoutUser(request):
    logout(request)
    return redirect('acces')