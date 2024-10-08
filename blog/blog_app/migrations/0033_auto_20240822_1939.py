# Generated by Django 3.1 on 2024-08-22 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0032_auto_20240822_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noteschat',
            name='username_user',
            field=models.CharField(max_length=100, unique=True, verbose_name='Username User'),
        ),
        migrations.AlterField(
            model_name='userschat',
            name='username_user1',
            field=models.CharField(max_length=50, verbose_name='Username User First'),
        ),
        migrations.AlterField(
            model_name='userschat',
            name='username_user2',
            field=models.CharField(max_length=50, verbose_name='Username User Second'),
        ),
    ]
