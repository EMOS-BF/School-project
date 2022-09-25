import django_filters
from .models import Eleve

class EleveFiltre(django_filters.FilterSet):
    class Meta:
        model= Eleve
        fields= '__all__'