# Generated by Django 3.1.6 on 2021-03-02 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_room', '0004_room_is_playing'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='songurl',
            field=models.CharField(default='https://www.youtube.com/watch?v=CtUIXnJKPgU', max_length=2000),
        ),
    ]
