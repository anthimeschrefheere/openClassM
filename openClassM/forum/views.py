#-*- coding: utf-8 -*-
from forum.models import Forum, Thread, Post, ThreadForm, PostForm
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def forum_dir(request):
    forum_list = Forum.objects.all()
    return render_to_response("forum/forum.html", {'forum_list' : forum_list})

def thread_dir(request, forum_id):
    thread_list = Thread.objects.filter( forum = forum_id )
    forum_info = Forum.objects.get( id = forum_id )
    if request.method == 'POST': # If the form has been submitted...
        form = ThreadForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            forum = Thread( forum = forum_info )
            form = ThreadForm(request.POST, instance = forum )
            form.save()
            return HttpResponseRedirect(reverse('forum.views.thread_dir', args=(forum_id,)))
    else:
        form = ThreadForm() # An unbound form   
    return render_to_response("forum/thread.html", 
                              {'thread_list' : thread_list, 
                               'forum_info' : forum_info,
                               'form': form}, 
                              context_instance=RequestContext(request) )

def post_dir(request, thread_id):
    thread_info = Thread.objects.get(pk=thread_id)
    post_list = Post.objects.filter( thread = thread_id )   
    if request.method == 'POST': 
        form = PostForm(request.POST) 
        if form.is_valid():
            thread = Post( thread = thread_info )
            form = PostForm(request.POST, instance = thread )
            form.save()
            return HttpResponseRedirect(reverse('forum.views.post_dir', args=(thread_id,)))
    else:
        form = PostForm()   
    return render_to_response("forum/post.html", 
                              {'post_list' : post_list, 
                               'thread_info' : thread_info, 
                               'form': form,},    
                              context_instance=RequestContext(request) )