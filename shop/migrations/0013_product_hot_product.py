# Generated by Django 3.2.4 on 2021-07-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_rename_tapstatus_product_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hot_product',
            field=models.BooleanField(default=False, verbose_name='להוסיף ל"מוצרים חמים" ?'),
        ),
    ]
