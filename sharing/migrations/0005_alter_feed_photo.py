# Generated by Django 4.1.3 on 2022-12-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharing', '0004_feed_person_fk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='Photo',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
