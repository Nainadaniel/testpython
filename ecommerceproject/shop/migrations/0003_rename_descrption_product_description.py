# Generated by Django 3.2.12 on 2022-08-05 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_rename_image_product_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='descrption',
            new_name='description',
        ),
    ]
