# Generated by Django 4.2.5 on 2023-09-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkservice_app', '0005_alter_subject_subjects_alter_task_school_class'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='subjects',
        ),
        migrations.AddField(
            model_name='schoolclass',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='homeworkservice_app.subject'),
        ),
    ]
