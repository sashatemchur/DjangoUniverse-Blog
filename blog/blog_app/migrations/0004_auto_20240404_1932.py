# Generated by Django 3.1 on 2024-04-04 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_auto_20240404_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userslistregisters',
            name='discription',
            field=models.CharField(max_length=250, null=True, verbose_name='Name and Surname'),
        ),
    ]
