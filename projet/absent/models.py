from django.db import models
from eleve.models import Eleve
from seance_cours.models import SeanceCours
from classe.models import Classe
# Create your models here.
class Absent(models.Model):
    Eleve=models.ForeignKey(Eleve,on_delete=models.CASCADE,verbose_name="Elève")
    Cours=models.ForeignKey(SeanceCours,on_delete=models.CASCADE,verbose_name="Cours")
    Classe = models.ForeignKey(Classe, on_delete=models.CASCADE, verbose_name="Classe",null=True)
    motif=models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Liste des Absents"

    def __str__(self):
        return str(self.Eleve) +" "+ str(self.Cours)