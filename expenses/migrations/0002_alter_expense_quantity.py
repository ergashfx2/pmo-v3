# Generated by Django 5.1 on 2024-08-09 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='quantity',
            field=models.BigIntegerField(),
        ),
    ]
