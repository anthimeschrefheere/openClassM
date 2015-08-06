#-*- coding: utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404
from tutoriels.models import Categorie, Article

def accueil_dir(request):
    return render_to_response("base.html")
# Create your views here.

def categorie_dir(request):
    categories_list = Categorie.objects.all()
    return render_to_response('tutoriels/categorie.html', {'categories_list': categories_list})


def article_dir(request, categorie_id):
    articles_list = Article.objects.filter( categorie = categorie_id )
    categories_list = Categorie.objects.filter( id = categorie_id )
    categories_list = categories_list[0]
    return render_to_response('tutoriels/article.html', {'articles_list': articles_list,'categorie_id': categorie_id,'categories_list': categories_list})

def article_read(request,categorie_id,article_id):
    article = get_object_or_404(Article, id=article_id)
    return render_to_response('tutoriels/article_read.html', {'article': article})