# Generated by Django 2.2 on 2019-04-03 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190403_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
