from django.urls import path
from . import views
#현재 폴더에서 view를 임포트해라!

app_name = 'posts'


urlpatterns = [
    path('', views.index, name='list'),
    path('write/', views.new, name='new'),    
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/update/', views.update, name='update'),


    path('naver/<str:q>/', views.naver),
]