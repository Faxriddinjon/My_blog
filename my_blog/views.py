from django.shortcuts import render, get_object_or_404
from .models import Blog

def Home(request):
    return render(request, 'home.html', {})

def Blogs(request):
    blogs=Blog.objects.all()

    return render(request,'blogs.html', {
        'blogs': blogs
    })

def Blogg(request, id):
    blog=get_object_or_404(Blog, pk=id)

    return render(request,'blog.html', {
        'blog': blog
    })