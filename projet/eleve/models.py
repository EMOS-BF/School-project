from django.db import models

# Create your models here.
class Eleve(models.Model):
    INE_eleve=models.CharField(max_length=200,verbose_name="INE de l'élève",unique=True,null=False)
    nom_eleve = models.CharField(max_length=200,verbose_name="Nom de l'élève",null=False)
    prenom_eleve = models.CharField(max_length=200, verbose_name="Prenom de l'élève",null=False)
    date_de_naissance = models.CharField(max_length=200,verbose_name="date de naissance de l'élève",null=True)
    filiere = models.CharField(max_length=200,verbose_name="filière de l'élève",null=False)
    classe = models.CharField(max_length=200,verbose_name="classe de l'élève",null=False)
    est_chef = models.BooleanField(default=False,verbose_name="Est chef de classe",null=False)
    class Meta:
        verbose_name="Liste des Elèves"

    def __str__(self):
        return str(self.nom_eleve) +"  "+ str(self.prenom_eleve)