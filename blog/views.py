from django.shortcuts import render, get_object_or_404
from .models import post

def posts(request):
    myPosts = post.objects.all()
    ctxt = {
        'myPosts' : myPosts,
    }
    return render(request, 'posts.html', ctxt)

def post_detail(request, post_id):
    myPost = get_object_or_404(post, pk = post_id)
    ctxt = {
        'myPost' : myPost,
    }
    return render(request, 'post_detail.html', ctxt)
