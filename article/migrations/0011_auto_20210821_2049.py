# Generated by Django 3.1.12 on 2021-08-21 18:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_remove_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=tinymce.models.HTMLField(null=True, verbose_name='Summary'),
        ),
    ]
