# Generated by Django 4.2.5 on 2023-10-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_club_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='場所')),
                ('image', models.ImageField(upload_to='images/', verbose_name='写真')),
                ('order', models.FloatField(default=0, verbose_name='優先順位')),
            ],
        ),
    ]