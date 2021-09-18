# Generated by Django 3.1.12 on 2021-09-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ebook',
            name='file',
        ),
        migrations.AddField(
            model_name='ebook',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='.', verbose_name='Cover'),
        ),
        migrations.AddField(
            model_name='ebook',
            name='file1',
            field=models.FileField(blank=True, null=True, upload_to='.', verbose_name='File1'),
        ),
        migrations.AddField(
            model_name='ebook',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to='.', verbose_name='File2'),
        ),
        migrations.AddField(
            model_name='ebook',
            name='file3',
            field=models.FileField(blank=True, null=True, upload_to='.', verbose_name='File3'),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Title'),
        ),
    ]