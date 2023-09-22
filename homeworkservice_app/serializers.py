from rest_framework import serializers
from .models import *
from rest_framework import status
from rest_framework.exceptions import NotFound


class TaskReadableSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.title')
    given_by = serializers.CharField(source='given_by.full_name')
    formatted_issued_date = serializers.SerializerMethodField()
    formatted_expire_date = serializers.SerializerMethodField()
    school_class = serializers.SlugRelatedField(
        many=True, queryset=SchoolClass.objects.all(), slug_field='title'
    )

    class Meta:
        model = Task
        exclude = [
            'issued_date',
            'expire_date',
        ]

    def get_formatted_issued_date(self, obj):
        date_str = obj.issued_date.strftime('The %dth of %B, %Y')
        return date_str.replace(" 0", " ")

    def get_formatted_expire_date(self, obj):
        date_str = obj.expire_date.strftime('The %dth of %B, %Y')
        return date_str.replace(" 0", " ")


class TaskSerializer(serializers.ModelSerializer):
    subject_title = serializers.CharField(write_only=True, required=False)
    school_class_title = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Task
        exclude = ('given_by', 'subject', 'school_class')

    def create(self, validated_data):
        user = self.context['request'].user
        given_by = Teacher.objects.get(user=user)
        school_classes = validated_data.pop('school_class', [])

        # Проверяем, был ли предоставлен subject_title
        subject_title = validated_data.pop('subject_title', None)
        if subject_title:
            try:
                subject = Subject.objects.get(title=subject_title)
                validated_data['subject'] = subject
            except Subject.DoesNotExist:
                raise NotFound(detail=f"Subject with title '{subject_title}' not found.", code=status.HTTP_404_NOT_FOUND)

        # Проверяем, был ли предоставлен school_class_title
        school_class_title = validated_data.pop('school_class_title', None)
        if school_class_title:
            try:
                school_class = SchoolClass.objects.get(title=school_class_title)
                school_classes.append(school_class)
            except SchoolClass.DoesNotExist:
                raise NotFound(detail=f"SchoolClass with title '{school_class_title}' not found.", code=status.HTTP_404_NOT_FOUND)

        task = Task.objects.create(given_by=given_by, **validated_data)
        task.school_class.set(school_classes)

        return task


class SubjectReadableSerializer(serializers.ModelSerializer):
    teacher = serializers.SlugRelatedField(
        many=True, queryset=Teacher.objects.all(), slug_field='full_name'
    )

    class Meta:
        model = Subject
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TeacherReadableSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    profile_image = serializers.CharField(source='profile_image.url')
    available_school_classes = serializers.SlugRelatedField(
        many=True, queryset=SchoolClass.objects.all(), slug_field='title'
    )

    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(
        max_length=None, use_url=True, required=False
    )

    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ('profile_image',)


class TeacherSchoolClassesSerializer(serializers.ModelSerializer):
    available_school_classes = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field='title'
    )

    class Meta:
        model = Teacher
        fields = ['available_school_classes']


class TeacherSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['title']


# class TeacherTasksSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = []


class SchoolClassReadableSerializer(serializers.ModelSerializer):
    class_teacher = serializers.CharField(source='class_teacher.full_name')
    subjects = serializers.SlugRelatedField(
        many=True, queryset=Subject.objects.all(), slug_field='title'
    )

    class Meta:
        model = SchoolClass
        fields = '__all__'


class SchoolClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = '__all__'
