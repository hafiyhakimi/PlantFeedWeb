# Generated by Django 4.1.3 on 2023-01-06 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0002_basket_basketqty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='basketqty',
        ),
    ]
