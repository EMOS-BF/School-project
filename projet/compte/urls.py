from django.urls import path
from . import views
urlpatterns=[
    path('incription/',views.incriptionPage,name='incription'),
    path('acces/',views.accesPage,name='acces'),
    path('quitter/',views.logoutUser,name='quitter')
]