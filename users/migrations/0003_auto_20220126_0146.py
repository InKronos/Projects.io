# Generated by Django 3.0.14 on 2022-01-26 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_is_developer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='avatar',
            field=models.CharField(default='./frontend/public/FileBase/defaulAvatar.bmp', max_length=100),
        ),
    ]
