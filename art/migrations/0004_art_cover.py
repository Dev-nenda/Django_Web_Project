# Generated by Django 4.2.2 on 2023-07-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0003_art_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='cover',
            field=models.URLField(blank=True, null=True),
        ),
    ]
