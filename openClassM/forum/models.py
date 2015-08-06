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
    title = "test"
    content = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        exclude = ('forum',)

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('thread',)
