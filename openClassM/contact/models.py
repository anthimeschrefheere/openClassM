from django.db import models
from django.forms import ModelForm

class Contact(models.Model):
    title = models.CharField(max_length=60)
    auteur = models.CharField(max_length=42)
    content = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title



