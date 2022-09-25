from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_module,name='module'),
    path('ajout_module/',views.Ajouter_module,name='ajout_module'),
    path('modifier_module/<str:pk>',views.modifier_module,name='modifier_module'),
    path('supprimer_module/<str:pk>',views.supprimer_module,name='supprimer_module'),

]