from django.urls import path
from . import views


urlpatterns = [
    path('all-tasks/', views.TaskListAPIView.as_view(), name='all-tasks'),
    path('all-tasks/create/', views.TaskCreateAPIView.as_view(), name='tasks-create'),
    path('all-tasks/<int:pk>/', views.TaskRetrieveAPIView.as_view(), name='tasks-retrieve'),
    path('all-tasks/<int:pk>/update/', views.TaskUpdateAPIView.as_view(), name='tasks-update'),
    path('all-tasks/<int:pk>/delete/', views.TaskDestroyAPIView.as_view(), name='tasks-delete'),
    path('all-subjects/', views.SubjectListAPIView.as_view(), name='all-subjects'),
    path('all-subjects/create/', views.SubjectCreateAPIView.as_view(), name='subjects-create'),
    path('all-subjects/<int:pk>/', views.SubjectRetrieveAPIView.as_view(), name='subjects-retrieve'),
    path('all-subjects/<int:pk>/update/', views.SubjectUpdateAPIView.as_view(), name='subjects-update'),
    path('all-subjects/<int:pk>/delete/', views.SubjectDestroyAPIView.as_view(), name='subjects-delete'),
]
