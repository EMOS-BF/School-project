from django.db import models

# Create your models here.
class Module(models.Model):
    Identifiant= models.CharField(max_length=200,verbose_name="Identifiant du module",unique=True,null=False)
    nom = models.CharField(max_length=200,verbose_name="Nom du module",null=False)
    nombre_heure= models.PositiveIntegerField(verbose_name="Nombre heure du module",null=False)
    semestre = models.PositiveIntegerField(null=False)
    class Meta:
        verbose_name="Liste des modules"

    def __str__(self):
        return self.nom