# Generated by Django 3.1 on 2024-05-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0014_remove_likeslistphoto_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likeslistphoto',
            name='id_photo',
            field=models.CharField(max_length=100, verbose_name='Id Photo'),
        ),
    ]
