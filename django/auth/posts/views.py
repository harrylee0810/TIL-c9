from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def new(request):
    if request.method == 'POST':
        #create
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
            #DB Insert
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

#Delete
def delete(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect('posts:list')
    
    else:
        return render(request, 'delete.html')


def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    
    if request.method == 'POST':
        #update
        post.title =request.POST.get('title')
        post.content =request.POST.get('content')
        post.save()    
        return redirect('posts:detail', post.pk)
    
    else:
        #edit
        return render(request, 'edit.html', {'post':post})
        


def comments_create(request, post_id):
    #댓글을 달 게시물에 대한 정보 가져오기
    post = Post.objects.get(pk=post_id)
    #form 태그에서 넘어온 댓글 내용 가져오기
    content = request.POST.get('content')
 
    #댓글 생성 및 저장 
    comment = Comment(post=post, content=content)
    comment.save()
    
    return redirect('posts:detail',post.pk)

def comments_delete(request, post_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    
    return redirect('posts:detail', post_id)
