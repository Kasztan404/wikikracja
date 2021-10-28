# Generated by Django 3.1.12 on 2021-10-13 15:54

import django.core.validators
from django.db import migrations, models
import glosowania.models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('glosowania', '0021_auto_20211013_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decyzja',
            name='znosi',
            field=models.CharField(blank=True, help_text='If the proposed law supersedes other bills, enter their numbers here.', max_length=50, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.'), glosowania.models.does_it_exist], verbose_name='Abolishes the rules'),
        ),
    ]
