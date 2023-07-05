from django.db import models

# Create your models here.
class Fondateur(models.Model):
    id_fondateur=models.AutoField(primary_key=True)
    nom=models.TextField(max_length=50)
    postnom=models.TextField(max_length=50)
    prenom=models.TextField(max_length=50)
    dateNaissance=models.DateField()
    photo=models.ImageField(upload_to="photo_fondateur")
    description=models.TextField(max_length=500)

    class Meta:
        db_table="t_fondateur"
    
    def __str__(self):
        return (f"{self.nom} {self.postnom} {self.prenom}")

class PartiPolitique(models.Model):
    id_parti=models.AutoField(primary_key=True)
    nom=models.TextField(max_length=50)
    annee_creation=models.DateField()
    logo=models.ImageField(upload_to="logo_partiPolitique")
    historique=models.TextField(max_length=500)
    service=models.TextField(max_length=250)
    fondateur=models.ForeignKey(Fondateur,on_delete=models.CASCADE)
    

    class Meta:
        db_table="t_partipolitique"
    def __str__(self):
        return self.nom
    
