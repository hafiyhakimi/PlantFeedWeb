# Generated by Django 4.1.3 on 2022-12-20 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marketplace', '0002_prodproduct_delete_marketplacecomment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productqty', models.IntegerField(default=0)),
                ('Person_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.prodproduct')),
            ],
            options={
                'db_table': 'basket',
            },
        ),
    ]
