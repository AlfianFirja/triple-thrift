# Generated by Django 5.1.1 on 2024-09-17 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productentry_delete_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productentry',
            old_name='ProductDescription',
            new_name='Product_Description',
        ),
        migrations.RenameField(
            model_name='productentry',
            old_name='ProductName',
            new_name='Product_Name',
        ),
        migrations.RenameField(
            model_name='productentry',
            old_name='ProductPrice',
            new_name='Product_Price',
        ),
    ]
