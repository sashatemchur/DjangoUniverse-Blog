# Generated by Django 3.1 on 2024-05-07 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0008_auto_20240427_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userslistphoto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
