import django_filters
from .models import Absent

class AbsentFiltre(django_filters.FilterSet):
    class Meta:
        model= Absent
        fields= '__all__'