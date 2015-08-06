from django.contrib import admin
from forum.models import Forum, Thread, Post

admin.site.register(Forum)
admin.site.register(Thread)
admin.site.register(Post)
# Register your models here.
