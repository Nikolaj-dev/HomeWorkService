# Generated by Django 4.2.5 on 2023-09-08 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='teacher_profile_images/')),
                ('phone_number', models.CharField(blank=True, max_length=12, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=256)),
                ('task_body', models.TextField()),
                ('issued_date', models.DateField(auto_now_add=True)),
                ('expire_date', models.DateField(auto_now_add=True)),
                ('given_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='homeworkservice_app.teacher')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeworkservice_app.subject')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='teacher',
            field=models.ManyToManyField(to='homeworkservice_app.teacher'),
        ),
    ]
