# Generated by Django 3.1.7 on 2021-04-05 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_cart_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cart_quantity',
        ),
    ]
