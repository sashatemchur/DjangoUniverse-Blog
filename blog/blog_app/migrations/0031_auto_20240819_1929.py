# Generated by Django 3.1 on 2024-08-19 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0030_auto_20240819_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteschat',
            name='notice_user',
            field=models.JSONField(blank=True, default=list, verbose_name='Notice User'),
        ),
    ]
