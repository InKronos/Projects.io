# Generated by Django 3.0.14 on 2022-01-12 01:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220111_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='applications',
            name='idUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]