
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='acceuil'),
    path('gestionIndividuel/<int:pk>/',views.gestionIndividuel,name='gestionIndividuel'),
    path('ajout_eleve/',views.Ajouter_eleve,name='ajout_eleve'),
    path('modifier_eleve/<str:pk>',views.modifier_eleve,name='modifier_eleve'),
    path('supprimer_eleve/<str:pk>',views.supprimer_eleve,name='supprimer_eleve'),

]
