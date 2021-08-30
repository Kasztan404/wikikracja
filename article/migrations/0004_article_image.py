# Generated by Django 3.1.12 on 2021-08-19 20:09

from django.db import migrations
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_remove_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Image'),
        ),
    ]