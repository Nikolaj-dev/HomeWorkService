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
    path('all-teachers/', views.TeacherListAPIView.as_view(), name='all-teachers'),
    path('all-teachers/create/', views.TeacherCreateAPIView.as_view(), name='teachers-create'),
    path('all-teachers/<int:pk>/', views.TeacherRetrieveAPIView.as_view(), name='teachers-retrieve'),
    path('all-teachers/<int:pk>/update/', views.TeacherUpdateAPIView.as_view(), name='teachers-update'),
    path('all-teachers/<int:pk>/delete/', views.TeacherDestroyAPIView.as_view(), name='teachers-delete'),
    path('all-school-classes/', views.SchoolClassListAPIView.as_view(), name='all-school-classes'),
    path('all-school-classes/create/', views.SchoolClassCreateAPIView.as_view(), name='school-classes-create'),
    path('all-school-classes/<int:pk>/', views.SchoolClassRetrieveAPIView.as_view(), name='school-classes-retrieve'),
    path('all-school-classes/<int:pk>/update/', views.SchoolClassUpdateAPIView.as_view(), name='school-classes-update'),
    path('all-school-classes/<int:pk>/delete/', views.SchoolClassDestroyAPIView.as_view(), name='school-classes-delete'),
    path('staff/teacher/', views.TeacherProfileAPIView.as_view(), name='teacher-profile'),
    path('staff/teacher/my-classes/', views.TeacherMySchoolClassesListAPIView.as_view(), name='teacher-school-classes'),
    path('staff/teacher/my-subjects/', views.TeacherMySubjectListAPIView.as_view(), name='teacher-subjects'),
    path('staff/teacher/my-tasks/', views.TeacherMyTaskListAPIView.as_view(), name='teacher-tasks'),
]
