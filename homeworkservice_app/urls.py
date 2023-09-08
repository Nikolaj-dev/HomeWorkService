from django.urls import path
from . import views


urlpatterns = [
    path('all-tasks/', views.TaskListAPIView.as_view(), name='all-tasks'),
    path('all-tasks/create/', views.TaskCreateAPIView.as_view(), name='tasks-create'),
    path('all-tasks/<int:pk>/', views.TaskRetrieveAPIView.as_view(), name='tasks-retrieve'),
    path('all-tasks/<int:pk>/update/', views.TaskUpdateAPIView.as_view(), name='tasks-update'),
    path('all-tasks/<int:pk>/delete/', views.TaskDestroyAPIView.as_view(), name='tasks-delete'),
]
