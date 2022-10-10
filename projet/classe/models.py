from django.db import models

# Create your models here.
class Classe(models.Model):
    nom = models.CharField(max_length=200,verbose_name="INE de l'élève",null=True)
    class Meta:
        verbose_name = "Liste des classe"

    def __str__(self):
        return str(self.nom)