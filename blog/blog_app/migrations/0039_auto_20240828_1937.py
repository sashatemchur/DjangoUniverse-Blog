# Generated by Django 3.1 on 2024-08-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0038_auto_20240826_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userschat',
            name='notice_user1',
            field=models.JSONField(blank=True, default=list, verbose_name='Notice User First'),
        ),
        migrations.AlterField(
            model_name='userschat',
            name='notice_user2',
            field=models.JSONField(blank=True, default=list, verbose_name='Notice User Second'),
        ),
    ]
