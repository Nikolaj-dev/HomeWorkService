from rest_framework import permissions
from .models import Subject


class IsTeacherPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, 'teacher')


class IsTeacherOfClass(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and hasattr(request.user, 'teacher'):
            teacher = request.user.teacher

            if 'school_class_title' in request.data:
                school_class_title = request.data['school_class_title']
                if teacher.available_school_classes.filter(title=school_class_title).exists():
                    return True

        return False


class IsTeacherAssociatedWithSubject(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and hasattr(request.user, 'teacher'):
            teacher = request.user.teacher

            subject_title = request.data.get('subject_title')
            if subject_title:
                if Subject.objects.filter(teacher=teacher, title=subject_title).exists():
                    return True

        return False


class IsTaskOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated and hasattr(request.user, 'teacher'):
            teacher = request.user.teacher

            return obj.given_by == teacher

        return False
