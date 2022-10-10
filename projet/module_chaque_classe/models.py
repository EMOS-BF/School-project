from django.db import models
from classe.models import Classe
from module.models import Module
# Create your models here.
class ClasseModule(models.Model):
    Classe = models.ForeignKey(Classe, on_delete=models.CASCADE, verbose_name="Classe",null=True)
    Module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="Classe")

    class Meta:
        verbose_name = "Liste des module en fonction des classes"

    def __str__(self):
        return str(self.Module) + " " + str(self.Classe)