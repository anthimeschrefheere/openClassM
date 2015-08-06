from django.contrib import admin
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display   = ('title', 'auteur','content', 'date','id')
    list_filter    = ('auteur','date',)
    date_hierarchy = 'date'
    ordering       = ('date','id', )
    search_fields  = ('title', 'content')

admin.site.register(Contact, ContactAdmin)