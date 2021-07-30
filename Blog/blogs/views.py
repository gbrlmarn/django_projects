from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogPostForm

def index(request):
    """Show all blog posts."""
    blogposts = BlogPost.objects.order_by('-date_added')
    context = {'blogposts' : blogposts}
    return render(request, 'blogs/index.html', context)

def new_blogpost(request):
    """Add a new blogpost"""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'form' : form}
    return render(request, 'blogs/new_blogpost.html', context)

def edit_blogpost(request, blogpost_id):
    blogpost = BlogPost.objects.get(id=blogpost_id)

    if request.method != 'POST':
        form = BlogPostForm(instance=blogpost)
    else:
        form = BlogPostForm(instance=blogpost, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    context = {'blogpost' : blogpost, 'form' : form}
    return render(request, 'blogs/edit_blogpost.html', context)

