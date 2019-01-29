from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    #DB Insert
    post = Post(title=title, content=content)
    post.save()
    return redirect(f'/posts/{post.pk}')

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'detail.html', {'post':post})


#Delete

def delete(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/posts/')


#Update
def edit(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'edit.html', {'post':post})


def update(request, post_id):
    #수정하는 코드
    post = Post.objects.get(pk=post_id)
    post.title =request.POST.get('title')
    post.content =request.POST.get('content')
    post.save()
    return redirect(f'/posts/{post_id}/')












def naver(request, q):
    return redirect(f'https://search.naver.com/search.naver?query={q}')


