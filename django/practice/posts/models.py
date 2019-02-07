from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, Thumbnail

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    #image = models.ImageField(blank=True)
    image = ProcessedImageField(
            upload_to='posts/images',
            processors=[Thumbnail(100,100)],
            format='JPEG',
            options={'quality':90}
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    
