from rest_framework import serializers
from .models import *


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
    class Meta:
        model = Task
        fields = '__all__'


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
