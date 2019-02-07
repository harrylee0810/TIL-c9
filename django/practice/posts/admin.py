from django.contrib import admin
from .models import Post, Comment

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_at','updated_at',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)