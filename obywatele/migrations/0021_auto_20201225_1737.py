# Generated by Django 3.1 on 2020-12-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obywatele', '0020_auto_20201225_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzytkownik',
            name='fb',
            field=models.CharField(blank=True, help_text='Link to your Facebook profile', max_length=500, null=True, verbose_name='Facebook'),
        ),
    ]