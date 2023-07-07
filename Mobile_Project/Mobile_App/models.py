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
    


class Membre(models.Model):
    id_membre=models.AutoField(primary_key=True)
    matricule=models.TextField(max_length=50)
    nom=models.TextField(max_length=100)
    post_nom=models.TextField(max_length=100)
    prenom=models.TextField(max_length=100)
    sexe=models.TextChoices("M","F")
    etat_civil=models.TextChoices("Marié", "Célibataire","Divorcé")
    lieu_naiss=models.TextField(max_length=50)
    date_naiss=models.DateField()
    numero_parcelle=models.TextField(max_length=10)
    niveau_etude=models.TextField(max_length=50)
    profession=models.TextField(max_length=50)
    niveau_membre=models.TextField(max_length=50)
    numero_telephone=models.IntegerField()
    email=models.EmailField(max_length=30)
    add_day=models.DateTimeField(auto_now_add=True)
    photo_profil=models.ImageField(upload_to="photo_membre")
    adresse=models.TextField(max_length=500)

    class Meta:
        db_table = 't_Membre'

    def __str__(self):
        return (f"{self.nom},{self.post_nom} {self.prenom} {self.niveau_membre}")

class Story(models.Model):
    id_story = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="story_images")
    username = models.TextField(max_length=50)
    class  Meta:
        db_table = 't_story'

    def __str__(self):
        return (f"{self.id_story}")   

class Post(models.Model):
    id_post = models.AutoField(primary_key= True)
    titre = models.TextField(max_length=150)
    username = models.TextField(max_length=50)  
    image_post = models.ImageField(upload_to="post_images")
    other = models.ImageField(upload_to="post_img")
    like  = models.IntegerField()
    commentaire = models.TextField(max_length=150)
    description = models.TextField(max_length=150)
    date_pub = models.DateField(auto_now_add=True)

    class  Meta:
        db_table = 't_post'

    def __str__(self):
        return (f"{self.titre}")
    
class Video(models.Model):
    id_video=models.AutoField(primary_key=True)
    titre=models.TextField(max_length=100)
    username=models.TextField(max_length=50)
    video=models.FileField(upload_to="videos")
    dateAjout=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="t_videos"

    def __str__(self):
        return (f"{self.titre}")
    
class Images(models.Model):
    id_image=models.AutoField(primary_key=True)
    images=models.ImageField(upload_to="images_liesPost")
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    class Meta:
        db_table="t_images"

class Commentaire(models.Model):
    id_commentaire=models.AutoField(primary_key=True)
    username=models.TextField(max_length=50)
    commentaire=models.TextField(max_length=750)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    date_Ajout=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="t_commentaires"

