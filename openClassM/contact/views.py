from contact.models import Contact
from django.shortcuts import render_to_response
from django.template import RequestContext

def contact(request):
    if request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid():
            form = ContactForm(request.POST)
            form.save()
            return HttpResponseRedirect(reverse('forum.views.post_dir', args=(thread_id,)))
    else:
        form = ContactForm()
    return render_to_response("contact/contact.html", {'form': form,},    
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