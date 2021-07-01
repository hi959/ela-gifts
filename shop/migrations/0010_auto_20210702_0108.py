# Generated by Django 3.2.4 on 2021-07-01 22:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_product_tapstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.FloatField(default=6, validators=[django.core.validators.MinValueValidator(5)], verbose_name='מחיר המבצע'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='tapStatus',
            field=models.BooleanField(default=False, verbose_name='לעשות מבצע ?'),
        ),
    ]
