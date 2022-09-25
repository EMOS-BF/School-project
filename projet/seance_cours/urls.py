from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_cours,name='cours'),
    path('ajout_cours/',views.Ajouter_cours,name='ajout_cours'),
    path('modifier_cours/<str:pk>',views.modifier_cours,name='modifier_cours'),
    path('supprimer_cours/<str:pk>',views.supprimer_cours,name='supprimer_cours'),

]