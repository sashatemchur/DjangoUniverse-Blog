# Generated by Django 3.1 on 2024-09-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0039_auto_20240828_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='userschat',
            name='notice_user_all',
            field=models.JSONField(blank=True, default=list, verbose_name='Notice User All'),
        ),
    ]
