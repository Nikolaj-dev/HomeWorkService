from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import TaskFilter
from .serializers import *


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskReadableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskReadableSerializer


class TaskUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskReadableSerializer


class SubjectListAPIView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectReadableSerializer


class SubjectCreateAPIView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectReadableSerializer


class SubjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectReadableSerializer



