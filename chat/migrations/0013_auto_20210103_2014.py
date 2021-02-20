# Generated by Django 3.1 on 2021-01-03 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0012_room_archived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='private',
        ),
        migrations.AddField(
            model_name='room',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]