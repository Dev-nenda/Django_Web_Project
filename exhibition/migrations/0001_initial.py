# Generated by Django 4.2.2 on 2023-07-04 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('schedule', models.CharField(max_length=50)),
                ('introduction', models.TextField()),
                ('artist', models.CharField(max_length=30)),
                ('locations', models.CharField(max_length=100)),
                ('ticketing', models.URLField(blank=True)),
                ('like_users', models.ManyToManyField(related_name='like_exhibitions', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibitions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='General_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('score', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general_reviews', to=settings.AUTH_USER_MODEL)),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='general_reviews', to='exhibition.exhibition')),
            ],
        ),
        migrations.CreateModel(
            name='Expert_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=100)),
                ('score', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_reviews', to=settings.AUTH_USER_MODEL)),
                ('exhibition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expert_reviews', to='exhibition.exhibition')),
            ],
        ),
    ]
