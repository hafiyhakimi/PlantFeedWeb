# Generated by Django 4.1.3 on 2023-01-20 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_rename_address_order_address_rename_cvv_order_cvv_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='CreditNumber',
            new_name='creditnumber',
        ),
    ]
