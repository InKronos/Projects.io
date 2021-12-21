# Generated by Django 3.0.14 on 2021-12-21 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211221_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingproject',
            name='idProject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Projects'),
        ),
        migrations.AlterField(
            model_name='ratingproject',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
    ]
