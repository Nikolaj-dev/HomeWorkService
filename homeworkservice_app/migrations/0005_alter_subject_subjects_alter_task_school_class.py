# Generated by Django 4.2.5 on 2023-09-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkservice_app', '0004_subject_subjects_schoolclass_task_school_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='homeworkservice_app.subject'),
        ),
        migrations.AlterField(
            model_name='task',
            name='school_class',
            field=models.ManyToManyField(to='homeworkservice_app.schoolclass'),
        ),
    ]
