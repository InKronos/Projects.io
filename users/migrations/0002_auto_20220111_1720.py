# Generated by Django 3.0.14 on 2022-01-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.FilePathField(blank=True, null=True),
        ),
    ]
