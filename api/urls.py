from django.urls import path
from . import views

urlpatterns = [
    path('tasks/all-tasks/', views.getTasks),
    path('tasks/create-task/', views.create_task),
    path('tasks/update-task/<str:pk>/', views.update_task),
    path('tasks/delete-task/<str:pk>/', views.delete_task),
    path('users/', views.getUsers),
]