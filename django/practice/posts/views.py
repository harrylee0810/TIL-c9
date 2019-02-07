from django.shortcuts import render, redirect
from .models import Post, Comment

# Create your views here.

def new(request):
    if request.method == 'POST':
        #create
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        post = Post(title=title, content=content, image=image)
        post.save()
        
        return redirect('posts:detail', post.pk)
    
    else:
        #new
        return render(request, 'new.html')
    

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})

def delete(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('posts:list')
        
    else:
        return render(request, 'delete.html')

def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail', post.pk)
    
    else:
        return render(request, 'edit.html', {'post':post})
    

def comments_create(request, post_id):
    post = Post.objects.get(pk=post_id)
    content = request.POST.get('content')
    
    comment = Comment(post=post, content=content)
    comment.save()
    
    return redirect('posts:detail', post.pk)

def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    return redirect('posts:detail', post_id)