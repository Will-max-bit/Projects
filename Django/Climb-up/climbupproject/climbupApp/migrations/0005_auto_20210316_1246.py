# Generated by Django 3.1.6 on 2021-03-16 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbupApp', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
