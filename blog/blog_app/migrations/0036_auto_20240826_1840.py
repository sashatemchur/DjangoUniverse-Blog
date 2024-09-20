# Generated by Django 3.1 on 2024-08-26 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0035_auto_20240823_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userschat',
            name='name_chat',
        ),
        migrations.AddField(
            model_name='userschat',
            name='name_chat_user1',
            field=models.CharField(blank=True, max_length=100, verbose_name='Name Chat User First'),
        ),
        migrations.AddField(
            model_name='userschat',
            name='name_chat_user2',
            field=models.CharField(blank=True, max_length=100, verbose_name='Name Chat User Second'),
        ),
    ]
