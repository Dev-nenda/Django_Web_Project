# Generated by Django 4.2.2 on 2023-07-10 01:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='followers',
        ),
        migrations.AddField(
            model_name='user',
            name='star',
            field=models.ManyToManyField(related_name='fans', to=settings.AUTH_USER_MODEL),
        ),
    ]
