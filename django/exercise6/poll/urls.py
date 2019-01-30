from django.urls import path
from . import views

app_name = 'poll'

urlpatterns = [
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:q_id>/', views.detail, name='detail'),
    path('', views.index, name='index'),
]