# Generated by Django 3.1 on 2024-08-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0037_auto_20240826_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userschat',
            name='notice_user1',
            field=models.JSONField(blank=True, max_length=1000000, verbose_name='Notice User First'),
        ),
        migrations.AlterField(
            model_name='userschat',
            name='notice_user2',
            field=models.JSONField(blank=True, max_length=1000000, verbose_name='Notice User Second'),
        ),
    ]
