# Generated by Django 2.1.8 on 2019-04-01 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0012_auto_20190401_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
