# Generated by Django 3.0.14 on 2022-01-26 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20220126_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='idOwner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
