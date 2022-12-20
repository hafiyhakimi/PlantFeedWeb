# Generated by Django 4.1.3 on 2022-12-20 08:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0003_category_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='prodProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productName', models.CharField(blank=True, max_length=255)),
                ('productDesc', models.CharField(blank=True, max_length=1500)),
                ('productCategory', models.CharField(blank=True, max_length=255)),
                ('productPrice', models.DecimalField(decimal_places=2, max_digits=4)),
                ('productPhoto', models.ImageField(null=True, upload_to='images/')),
                ('productRating', models.IntegerField(default=0)),
                ('timePosted', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'prodProduct',
            },
        ),
        migrations.DeleteModel(
            name='MarketplaceComment',
        ),
        migrations.RemoveField(
            model_name='marketplacefeed',
            name='Person_fk',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='MarketplaceFeed',
        ),
    ]