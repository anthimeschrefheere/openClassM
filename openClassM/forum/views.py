from django.shortcuts import render
from forum.models import Forum, Thread, Post

from django.shortcuts import render_to_response
from django.template import RequestContext

def forum_dir(request):
    forum_list = Forum.objects.all()
    return render_to_response("forum/forum.html", 
                              {'forum_list' : forum_list})

def thread_dir(request, forum_id):
    thread_list = Thread.objects.filter( forum = forum_id )
    p = Forum.objects.get( id = forum_id )
    forum_title = p.title
    return render_to_response("forum/thread.html", 
                              {'thread_list' : thread_list, 
                               'forum_title' : forum_title, 
                               'forum_id': forum_id}, 
                               context_instance=RequestContext(request) )

def post_dir(request, thread_id):
    thread_info = Thread.objects.get(pk=thread_id)
    post_list = Post.objects.filter( thread = thread_id )
    return render_to_response("forum/post.html", 
                              {'post_list' : post_list, 'thread_info' : thread_info,},    
                              context_instance=RequestContext(request) )
