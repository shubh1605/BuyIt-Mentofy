# Generated by Django 3.1.7 on 2021-04-05 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0005_auto_20210406_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]