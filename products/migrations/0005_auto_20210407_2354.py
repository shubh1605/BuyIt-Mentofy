# Generated by Django 3.1.7 on 2021-04-07 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image5',
        ),
    ]
