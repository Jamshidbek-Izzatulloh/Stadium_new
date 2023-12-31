# Generated by Django 4.2.3 on 2023-07-28 10:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('lname', models.CharField(default='', max_length=100)),
                ('date_of_birth', models.DateField(default=datetime.datetime.now)),
                ('address', models.CharField(max_length=150)),
                ('contact', models.CharField(default='', max_length=30)),
                ('email', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='User_photo/%Y/%m/%d')),
            ],
            options={
                'db_table': 'user_model',
            },
        ),
    ]
