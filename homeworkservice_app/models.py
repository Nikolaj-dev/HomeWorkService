from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    theme = models.CharField(max_length=256)
    task_body = models.TextField()
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    issued_date = models.DateField(auto_now_add=True)
    expire_date = models.DateField()
    given_by = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    school_class = models.ManyToManyField('SchoolClass')

    def __str__(self):
        return self.theme


class Subject(models.Model):
    title = models.CharField(max_length=128)
    teacher = models.ManyToManyField('Teacher')

    def __str__(self):
        return self.title


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=128)
    profile_image = models.ImageField(upload_to='teacher_profile_images/', null=True, blank=True)
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.full_name


class SchoolClass(models.Model):
    title = models.CharField(max_length=64)
    class_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True)
    subjects = models.ManyToManyField('Subject', blank=True)

    def __str__(self):
        return self.title


