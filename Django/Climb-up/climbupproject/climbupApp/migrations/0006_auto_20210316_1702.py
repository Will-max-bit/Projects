# Generated by Django 3.1.6 on 2021-03-17 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climbupApp', '0005_auto_20210316_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
