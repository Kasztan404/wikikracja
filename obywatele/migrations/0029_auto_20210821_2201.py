# Generated by Django 3.1.12 on 2021-08-21 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('obywatele', '0028_auto_20210103_1959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uzytkownik',
            options={'verbose_name': 'Citizen', 'verbose_name_plural': 'Citizens'},
        ),
    ]