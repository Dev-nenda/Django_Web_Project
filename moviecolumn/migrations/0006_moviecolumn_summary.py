# Generated by Django 4.2.2 on 2023-07-14 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviecolumn', '0005_moviecolumn_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviecolumn',
            name='summary',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
