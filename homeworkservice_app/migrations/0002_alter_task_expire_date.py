# Generated by Django 4.2.5 on 2023-09-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeworkservice_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='expire_date',
            field=models.DateField(auto_now=True),
        ),
    ]
