# Generated by Django 4.2.5 on 2023-09-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkservice_app', '0006_remove_subject_subjects_schoolclass_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='available_school_classes',
            field=models.ManyToManyField(to='homeworkservice_app.schoolclass'),
        ),
    ]