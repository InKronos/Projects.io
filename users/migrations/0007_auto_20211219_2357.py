# Generated by Django 3.0.14 on 2021-12-19 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20211219_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='folder',
            field=models.FilePathField(allow_folders=True, path='./FilesBase'),
        ),
    ]
