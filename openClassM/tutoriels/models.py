from django.db import models

class Categorie(models.Model):
    title = models.CharField(max_length=30)
    def __unicode__(self):
        return self.title  
    def __str__(self):
        return self.title

class Article(models.Model):
    categorie = models.ForeignKey(Categorie)
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")

    def __unicode__(self):
        return self.titre
    def __str__(self):
        return self.titre