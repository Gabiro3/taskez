from django.urls import path
from . import views

urlpatterns = [
    path('users/get-user/<str:email>/', views.getUser, name='get-user'),
    path('tasks/all-tasks/', views.getTasks),
    path('tasks/create-task/', views.create_task),
    path('tasks/update-task/<str:pk>/', views.update_task),
    path('tasks/delete-task/<str:pk>/', views.delete_task),
    
    path('groups/user-groups', views.get_groups, name='get-groups'),
    path('groups/create-group/', views.create_group, name='create-group'),
    path('groups/update-group/<str:pk>/', views.update_group, name='update-group'),
    path('groups/delete-group/<str:pk>/', views.delete_group, name='delete-group'),


    path('invitations/all', views.view_invitations, name='view-invitations'),
    path('invitations/create-invitation/', views.create_invitation, name='create-invitation'),
    path('invitations/delete-invitation/<str:pk>/', views.delete_invitation, name='delete-invitation'),
    path('invitations/accept-invitation/<str:pk>/', views.accept_invitation, name='accept-invitation'),
]