# Generated by Django 2.1.8 on 2019-04-01 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_auto_20190401_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(null=True),
        ),
    ]
