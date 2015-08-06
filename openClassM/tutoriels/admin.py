from django.contrib import admin
from tutoriels.models import Categorie, Article

class CategorieAdmin(admin.ModelAdmin):
    list_display   = ('title','id')
    search_fields  = ('title','id')

class ArticleAdmin(admin.ModelAdmin):
    list_display   = ('titre', 'auteur', 'date','categorie','id')
    list_filter    = ('auteur','categorie',)
    date_hierarchy = 'date'
    ordering       = ('date','categorie', )
    search_fields  = ('titre', 'contenu')

admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, ArticleAdmin)