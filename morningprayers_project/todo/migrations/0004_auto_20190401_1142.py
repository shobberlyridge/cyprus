# Generated by Django 2.1.8 on 2019-04-01 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20190401_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
