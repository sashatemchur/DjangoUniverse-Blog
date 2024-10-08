# Generated by Django 3.1 on 2024-03-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsersListRegisters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=500, verbose_name='Name and Surname')),
                ('username', models.CharField(max_length=500, verbose_name='Username')),
                ('password', models.IntegerField(verbose_name='Passwords')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
    ]
