from django.urls import path
from . import views

urlpatterns = [
    path('users/get-user/<str:email>/', views.getUser, name='get-user'),
    path('users/related-users/', views.getRelatedUsers),
    path('users/delete-user/<str:pk>/', views.deleteUser),
    path('users/update-profile/', views.update_user),
    path('users/chat-users/', views.get_chat_users),

    path('tasks/all-tasks/<int:activity_id>/', views.getTasks, name='fetch-tasks'),
    path('tasks/pending/<int:activity_id>/', views.getPendingTasks, name='pending-tasks'),
    path('tasks/completed/<int:activity_id>/', views.getCompletedTasks, name='completed-tasks'),

    path('activities/create-activity', views.createActivity, name='create-activity'),
    path('activities/all', views.getActivities, name='get-activities'),
    path('activities/delete/<str:pk>/', views.delete_activity),
    path('activities/add-task/<str:activity_id>/', views.addTasksToActivity),
    path('tasks/create-task/<str:activity_name>/', views.create_task),
    path('tasks/update-task/<str:pk>/', views.update_task),
    path('tasks/delete-task/<str:pk>/', views.delete_task),
    
    path('groups/user-groups', views.get_groups, name='get-groups'),
    path('groups/create-group/', views.create_group, name='create-group'),
    path('groups/update-group/<str:pk>/', views.update_group, name='update-group'),
    path('groups/delete-group/<str:pk>/', views.delete_group, name='delete-group'),
    path('groups/participants/<int:group_id>', views.get_group_participants),


    path('invitations/all', views.view_invitations, name='view-invitations'),
    path('invitations/create-invitation/', views.create_invitation, name='create-invitation'),
    path('invitations/delete-invitation/<str:pk>/', views.delete_invitation, name='delete-invitation'),
    path('invitations/accept-invitation/<str:pk>/', views.accept_invitation, name='accept-invitation'),


    path('analytics/activities/completion-rate/<int:activity_id>/', views.get_activity_completion_rate),
    path('analytics/tasks/priority-rate/', views.get_task_priority_completion_rate),
    path('analytics/user/success-rate', views.daily_success_rate)
]