# Generated by Django 2.1.8 on 2019-04-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_todo_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
