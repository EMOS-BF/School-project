from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_eleve_autoriser_à_composer,name="autoriser"),
]