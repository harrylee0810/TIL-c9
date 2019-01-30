from django.contrib import admin
from .models import Post, Comment


#내용도 같이 보이게 admin 페이지를 커스터마이징 할 필요 있음
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content',)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)