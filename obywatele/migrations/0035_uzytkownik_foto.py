# Generated by Django 3.1.12 on 2021-09-15 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obywatele', '0034_remove_uzytkownik_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzytkownik',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='.', verbose_name='Foto'),
        ),
    ]