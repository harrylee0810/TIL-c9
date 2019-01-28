from django.shortcuts import render
from .models import Post
import random

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    #데이터베이스에 작성하는  코드 작성
    #Post라는 클래스는 views.py에 임포트 해야 함.
    post = Post(title=title, content=content)
    post.save()
    return render(request, 'create.html')


def index(request):
    #All 모든 포스트불러오기
    posts = Post.objects.all()
    
    return render(request, 'index.html', {'posts':posts})











def tmr_lunch(request):
    lunch = ["제육덥밥","돌솥비빔밥","김치소면"]
    student = ["진민재","하창언","권민재","이현수"]
    selected_menu = random.choice(lunch)
    selected_student  = random.choice(student)
    return render(request, 'lunch.html', {'lunch':selected_menu, 'student':selected_student})