# Generated by Django 3.2.9 on 2022-01-17 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0013_remove_group_feed_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupsharing',
            name='GGraph',
        ),
        migrations.AlterField(
            model_name='groupsharing',
            name='GPhoto',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='groupsharing',
            name='GVideo',
            field=models.FileField(null=True, upload_to='videomedia/'),
        ),
    ]
