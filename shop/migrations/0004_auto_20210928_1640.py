# Generated by Django 3.2.4 on 2021-09-28 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210928_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='subimage1',
            field=models.ImageField(blank=True, upload_to='product_sub_images', verbose_name='תמונה נוספת 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='subimage2',
            field=models.ImageField(blank=True, upload_to='product_sub_images', verbose_name='תמונה נוספת 2'),
        ),
    ]
