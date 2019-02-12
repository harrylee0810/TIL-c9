from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # article = form.save()
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            article = Article.objects.create(title=title, content=content)
        return redirect('articles:detail', article.pk)
    
    else:
        form = ArticleForm()
    return render(request, 'form.html' , {'form':form})


def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article' : article})
    
def update(request, article_id):
    article = Article.objects.get(pk=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    
    else:
        form = ArticleForm(instance=article)
        
    return render(request, 'form.html', {'form':form})
    
    
    
    
    
    
    
    
    