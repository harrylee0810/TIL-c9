from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

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