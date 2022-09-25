from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_absent,name='absent'),
    path('ajout_absent/',views.Ajouter_absent,name='ajout_absent'),
    path('modifier_absent/<str:pk>',views.modifier_absent,name='modifier_absent'),
    path('supprimer_absent/<str:pk>',views.supprimer_absent,name='supprimer_absent'),

]