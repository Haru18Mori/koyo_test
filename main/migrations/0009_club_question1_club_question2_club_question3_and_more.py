# Generated by Django 4.2.5 on 2023-10-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_club_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='question1',
            field=models.TextField(default='①今回の音展での出し物で特にこれといった推しがあれば教えてください', max_length=300, verbose_name='①今回の音展での出し物で特にこれといった推しがあれば教えてください'),
        ),
        migrations.AddField(
            model_name='club',
            name='question2',
            field=models.TextField(default='②部長の趣味を教えてください', max_length=300, verbose_name='②部長の趣味を教えてください'),
        ),
        migrations.AddField(
            model_name='club',
            name='question3',
            field=models.TextField(default='③なぜこの部活に参加しようと思ったのですか?', max_length=300, verbose_name='③なぜこの部活に参加しようと思ったのですか?'),
        ),
        migrations.AddField(
            model_name='club',
            name='question4',
            field=models.TextField(default='④部活動の中で一番やりがいを感じていることはどう言うことですか?', max_length=300, verbose_name='④部活動の中で一番やりがいを感じていることはどう言うことですか?'),
        ),
    ]
