# Generated by Django 4.1.3 on 2023-02-08 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0014_auto_20220117_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmember',
            name='Userlevel',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='groupsharing',
            name='Status',
            field=models.IntegerField(null=True),
        ),
    ]