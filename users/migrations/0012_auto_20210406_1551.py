# Generated by Django 3.1.7 on 2021-04-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210406_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_ordered',
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_placed',
            field=models.BooleanField(default=False),
        ),
    ]
