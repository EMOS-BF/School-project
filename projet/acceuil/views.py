from django.shortcuts import render

# Create your views here.
def acceuil(request):
    return render(request,'acceuil/acceuil1.html')