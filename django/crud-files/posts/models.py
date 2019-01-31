from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    image =  ProcessedImageField(
            upload_to='posts/images', #저장위치
            processors=[ResizeToFill(300,300)],#처리할작업 목록
            format='JPEG',#저장포맷(확장자)
            options={'quality':90}, #저장 포맷 관련 옵션(JPEG 압축률 설정)
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


#Post : Comment = 1 : N
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    








    
#1. Create
#post = Post(title='Hello',content='world!')
#post.save()

#2. Read
#2.1 All
#posts = Post.objects.all()
#2.2 Get one
#posts = Post.objects.get(pk=1)