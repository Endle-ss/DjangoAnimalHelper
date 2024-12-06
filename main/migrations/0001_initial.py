# Generated by Django 5.1.3 on 2024-11-30 15:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('role', models.CharField(max_length=50)),
                ('rating', models.FloatField(default=0.0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=50)),
                ('points', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='SearchCard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name_animal', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('animal_type', models.CharField(max_length=30)),
                ('describe_animal', models.TextField()),
                ('last_seen_location', models.CharField(max_length=255)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='SearchActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('status_activity', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customuser')),
                ('search_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.searchcard')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('target_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints_against_user', to='main.customuser')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaints_by_user', to='main.customuser')),
                ('search_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.searchcard')),
            ],
        ),
        migrations.CreateModel(
            name='CardMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customuser')),
                ('search_card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.searchcard')),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('search_card_created', models.IntegerField(default=0)),
                ('animals_found', models.IntegerField(default=0)),
                ('search_count', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customuser')),
            ],
        ),
    ]