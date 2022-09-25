from django.db import models
from module.models import Module
# Create your models here.
class SeanceCours(models.Model):
    Enseignant= models.CharField(max_length=200,null=False)
    nombre_heure= models.PositiveIntegerField(verbose_name="Nombre heure du cours",null=False)
    date =models.DateTimeField(auto_now_add=True,null=False)
    Module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name="Module",null=True)

    class Meta:
        verbose_name = "Liste des cours"

    def __str__(self):
        return str(self.Module) + " " + str(self.Enseignant)