# Generated by Django 3.0.14 on 2021-12-19 21:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=255)),
            ],
            options={
                'verbose_name': 'Ogłoszenie',
                'verbose_name_plural': 'Ogłoszenia',
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'verbose_name': 'Stanowisko',
                'verbose_name_plural': 'Stanowiska',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
            options={
                'verbose_name': 'Rola',
                'verbose_name_plural': 'Role',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('name', models.TextField(max_length=50, unique=True)),
                ('avatar', models.ImageField(height_field=255, upload_to='', width_field=255)),
                ('description', models.TextField(max_length=255)),
                ('averageRate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('idRole', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='users.Roles')),
            ],
            options={
                'verbose_name': 'Użytkownik',
                'verbose_name_plural': 'Użytkownicy',
            },
        ),
        migrations.CreateModel(
            name='SkillsDeveloper',
            fields=[
                ('idUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.Users')),
                ('Cpp', models.BooleanField(default=False)),
                ('CSharp', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Umiejętności dewelopera',
                'verbose_name_plural': 'Umiejętności deweloperów',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=50, unique=True)),
                ('stage', models.CharField(choices=[('BS', 'BrainStorm'), ('EB', 'EarlyBird'), ('PG', 'PlayGround')], default='BS', max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('folder', models.FilePathField(allow_folders=True)),
                ('averageRate', models.DecimalField(decimal_places=2, max_digits=3)),
                ('idOwner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Users')),
            ],
            options={
                'verbose_name': 'Projekt',
                'verbose_name_plural': 'Projekty',
            },
        ),
        migrations.CreateModel(
            name='CollaboratorsProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPosition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Positions')),
                ('idProject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Projects')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
            options={
                'verbose_name': 'Twórca',
                'verbose_name_plural': 'Twórcy',
            },
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=255)),
                ('acceptionState', models.CharField(choices=[('P', 'pending'), ('A', 'accepted'), ('R', 'rejected')], default='P', max_length=255)),
                ('idAdvertisement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Advertisements')),
            ],
            options={
                'verbose_name': 'Zgłoszenie',
                'verbose_name_plural': 'Zgłoszenia',
            },
        ),
        migrations.AddField(
            model_name='advertisements',
            name='idPosition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Positions'),
        ),
        migrations.AddField(
            model_name='advertisements',
            name='idProject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Projects'),
        ),
        migrations.CreateModel(
            name='RatingUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('idRatedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratingusers_requests_created', to='users.Users')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
            options={
                'verbose_name': 'Ocena użytkownika',
                'verbose_name_plural': 'Oceny użytkowników',
                'unique_together': {('idRatedUser', 'idUser')},
            },
        ),
        migrations.CreateModel(
            name='RatingProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('idProject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Projects')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
            options={
                'verbose_name': 'Ocena projektu',
                'verbose_name_plural': 'Oceny projektów',
                'unique_together': {('idProject', 'idUser')},
            },
        ),
    ]