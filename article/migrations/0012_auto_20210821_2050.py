# Generated by Django 3.1.12 on 2021-08-21 18:50

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20210821_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=tinymce.models.HTMLField(null=True, verbose_name='Body'),
        ),
    ]
