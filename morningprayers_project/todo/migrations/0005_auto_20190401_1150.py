# Generated by Django 2.1.8 on 2019-04-01 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20190401_1142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='created',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='updated',
        ),
    ]
