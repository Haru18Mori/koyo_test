# Generated by Django 4.2.5 on 2023-10-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='slug',
            field=models.SlugField(max_length=256, null=True, unique=True),
        ),
    ]