from django.shortcuts import render, redirect
from .models import Question, Choice
# Create your views here.

def new(request):
    return render(request, 'new1.html')

def create(request):
    title = request.POST.get('title')
    question = Question(title=title)
    question.save()
    return redirect('poll:detail', question.pk)

def index(request):
    questions = Question.objects.all()
    return render(request, 'index1.html', {'questions':questions})

def detail(request, q_id):
    question = Question.objects.get(pk=q_id)
    return render(request, 'detail1.html', {'question': question})