# Generated by Django 3.2.4 on 2021-07-05 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20210704_1617'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='tapStatus',
            new_name='sale',
        ),
    ]
