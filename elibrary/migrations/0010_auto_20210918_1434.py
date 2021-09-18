# Generated by Django 3.1.12 on 2021-09-18 12:34

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('elibrary', '0009_auto_20210918_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tag',
            field=taggit.managers.TaggableManager(blank=True, help_text='Groups of characters which appear between double quotes take precedence as multi-word tags (so double quoted tag names may contain commas). An unclosed double quote will be ignored. Otherwise, if there are any unquoted commas in the input, it will be treated as comma-delimited. If not, it will be treated as space-delimited.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]