from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .filters import TaskFilter, SubjectFilter, TeacherFilter, SchoolClassFilter
from .serializers import *
from rest_framework.views import APIView


class TaskListAPIView(generics.ListAPIView):
    # authentication_classes = [JWTAuthentication, ]
    # permission_classes = [IsAuthenticated, ]
    queryset = Task.objects.all()
    serializer_class = TaskReadableSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TaskFilter
    search_fields = ['theme', 'school_class__title']


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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = SubjectFilter
    ordering_fields = '__all__'
    search_fields = ['title', 'teacher__full_name']


class SubjectCreateAPIView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectReadableSerializer


class SubjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectReadableSerializer


class SubjectDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectReadableSerializer


class TeacherListAPIView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherReadableSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = TeacherFilter
    ordering_fields = ['full_name',]


class TeacherCreateAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherReadableSerializer


class TeacherUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    partial = True

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            # Check if a new profile image was provided
            profile_image = request.data.get('profile_image')
            if profile_image:
                instance.profile_image = profile_image
                instance.save()

            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TeacherDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherReadableSerializer


class SchoolClassListAPIView(generics.ListAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassReadableSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = SchoolClassFilter
    ordering_fields = ['title', ]
    search_fields = ['title', ]


class SchoolClassCreateAPIView(generics.CreateAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer


class SchoolClassRetrieveAPIView(generics.RetrieveAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassReadableSerializer


class SchoolClassUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassReadableSerializer


class SchoolClassDestroyAPIView(generics.RetrieveDestroyAPIView):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassReadableSerializer


class TeacherProfileAPIView(APIView):
    serializer_class = TeacherReadableSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get the user's teacher profile
        teacher_profile = Teacher.objects.filter(user=request.user).first()

        if teacher_profile:
            # Serialize the teacher profile data
            serializer = self.serializer_class(teacher_profile)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Teacher profile not found.'}, status=status.HTTP_404_NOT_FOUND)


class TeacherMySchoolClassesAPIView(generics.RetrieveAPIView):
    serializer_class = TeacherSchoolClassesSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Retrieve the Teacher object associated with the current user
        return Teacher.objects.get(user=self.request.user)

    def get(self, request):
        teacher = self.get_object()

        # Access the available_school_classes field directly from the teacher object
        available_school_classes = teacher.available_school_classes.all()

        serializer = self.serializer_class({'available_school_classes': available_school_classes})
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherMySubjectsAPIView(generics.ListAPIView):
    serializer_class = TeacherSubjectsSerializer

    def get_queryset(self):
        teacher = Teacher.objects.filter(user=self.request.user).first()
        subjects = Subject.objects.filter(teacher=teacher).all()
        return subjects
