# Generated by Django 2.1.8 on 2019-04-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20190401_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='target_completion_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
