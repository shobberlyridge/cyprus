# Generated by Django 2.1.8 on 2019-04-01 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20190401_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
