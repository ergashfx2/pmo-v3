# Generated by Django 5.1 on 2024-08-12 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_remove_project_author_alter_project_team_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
    ]
