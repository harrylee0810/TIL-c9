from django.urls import path
from . import views
#현재 폴더에서 view를 임포트해라!

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('new/', views.new),
]