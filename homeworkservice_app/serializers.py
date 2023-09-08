from rest_framework import serializers
from .models import *


class TaskReadableSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.title')
    given_by = serializers.CharField(source='given_by.full_name')
    formatted_issued_date = serializers.SerializerMethodField()
    formatted_expire_date = serializers.SerializerMethodField()

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
