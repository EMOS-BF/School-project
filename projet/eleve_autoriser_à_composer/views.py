from django.shortcuts import render
# Create your views here.
def list_eleve_autoriser_à_composer(request):
    return render(request,'eleve_autoriser_à_composer/list_eleve_autoriser_à_composer.html')