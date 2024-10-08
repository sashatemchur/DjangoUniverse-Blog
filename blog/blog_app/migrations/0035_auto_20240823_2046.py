# Generated by Django 3.1 on 2024-08-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0034_auto_20240823_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userschat',
            name='photo_chat_user1',
            field=models.ImageField(upload_to='blog_app/static/blog_app/img/', verbose_name='Photo User Chat First'),
        ),
        migrations.AlterField(
            model_name='userschat',
            name='photo_chat_user2',
            field=models.ImageField(upload_to='blog_app/static/blog_app/img/', verbose_name='Photo User Chat Second'),
        ),
    ]
