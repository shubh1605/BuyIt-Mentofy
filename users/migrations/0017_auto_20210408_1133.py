# Generated by Django 3.1.7 on 2021-04-08 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210407_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_placed_on',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user_info',
            name='order_placed_on',
            field=models.DateField(blank=True, null=True),
        ),
    ]
