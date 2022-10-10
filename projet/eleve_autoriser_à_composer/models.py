from django.db import models
from eleve.models import Eleve
from module.models import Module
from classe.models import Classe
# Create your models here.
class Eleve_autoriser_composer(models.Model):
    Eleve= models.ForeignKey(Eleve,on_delete=models.CASCADE,verbose_name="Elève",null=False)
    Module=models.ForeignKey(Module,on_delete=models.CASCADE,verbose_name="Module",null=False)
    Classe = models.ForeignKey(Classe, on_delete=models.CASCADE, verbose_name="Classe",null=True)

    class Meta:
        verbose_name = "Liste des Elèves autorisés à composer un devoir"

    def __str__(self):
        return self.Eleve +" "+ self.Module