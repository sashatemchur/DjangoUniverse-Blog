# Generated by Django 3.1 on 2024-05-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0009_auto_20240507_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='userslistphoto',
            name='id_photo',
            field=models.CharField(default=12, max_length=100, verbose_name='Id Photo'),
            preserve_default=False,
        ),
    ]
