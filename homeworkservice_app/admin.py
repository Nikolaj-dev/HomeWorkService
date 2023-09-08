from django.contrib import admin
from .models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'given_by',
        'theme',
        'issued_date',
    )
    list_filter = (
        'subject',
        'issued_date',
        'given_by',
    )
    search_fields = (
        'theme',
    )


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
    search_fields = (
        'title',
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'phone_number',
        'email',
    )
    search_fields = (
        'full_name',
    )
