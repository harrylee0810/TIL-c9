from . import views
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('', views.index, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
]