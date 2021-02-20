# Generated by Django 3.1 on 2021-01-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glosowania', '0005_auto_20201122_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='decyzja',
            name='title',
            field=models.TextField(help_text='Enter short title describing new law.', max_length=200, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='decyzja',
            name='tresc',
            field=models.TextField(help_text='Enter the exact wording of the law as it is to be applied.', max_length=500, null=True, verbose_name='Law text'),
        ),
    ]
