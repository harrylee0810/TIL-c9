from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create),
    path('new/', views.new),
    path('', views.index),
    path('<int:student_id>', views.detail),
    path('delete/<int:student_id>/', views.delete),
    path('edit/<int:student_id>/', views.edit),
    path('update/<int:student_id>/', views.update),
]