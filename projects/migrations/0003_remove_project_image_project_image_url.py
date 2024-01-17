# Generated by Django 5.0.1 on 2024-01-17 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_image_project_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AddField(
            model_name='project',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
