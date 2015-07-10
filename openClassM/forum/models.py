from django.db import models
from django.forms import ModelForm

class Forum(models.Model):  
    title = models.CharField(max_length=60)
    def __unicode__(self):
        return self.title

class Thread(models.Model):
    forum = models.ForeignKey(Forum)
    title = models.CharField(max_length=60)
    content = models.TextField(max_length=10000)    
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Post(models.Model):
    thread = models.ForeignKey(Thread)
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title


Forum(title="Forum sur les maths" ).save()
Forum(title="Forum sur la physique" ).save()
Forum(title="Forum sur l'informatique" ).save()
