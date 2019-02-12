from django.urls import path
from . import views
#현재 폴더에서 view를 임포트해라!

app_name = 'posts'


urlpatterns = [
    path('', views.index, name='list'), #GET : 모든 포스트의리스트를 가져와라
    path('new/', views.new, name='new'), #GET(new), POST(create) :새로운 페이지를 가져와라
    #path('create/', views.create, name='create'), #POST(create): create라는 동사를 uri주소로 넣는건 아키텍쳐에 바람직하지않으므
    path('<int:post_id>/', views.detail, name='detail'), #GET
    path('<int:post_id>/delete/', views.delete, name='delete'), #GET(conifrm) POST(delete) 사용
    path('<int:post_id>/edit/', views.edit, name='edit'), #GET(edit), POST(update)
    #path('<int:post_id>/update/', views.update, name='update'),
    
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    # path('naver/<str:q>/', views.naver),
]