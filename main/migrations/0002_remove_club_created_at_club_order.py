# Generated by Django 4.2.5 on 2023-09-09 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='created_at',
        ),
        migrations.AddField(
            model_name='club',
            name='order',
            field=models.FloatField(default=0, verbose_name='優先順位'),
        ),
    ]
