# Generated by Django 4.1.5 on 2023-02-08 14:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_remove_rejecttopic_topic_ptr_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TopicName', models.CharField(max_length=150)),
                ('Status', models.CharField(default='Suggested', max_length=100)),
            ],
            options={
                'db_table': 'TopicComponent',
            },
        ),
        migrations.RemoveField(
            model_name='usertopic',
            name='Approval',
        ),
        migrations.RemoveField(
            model_name='usertopic',
            name='TopicName',
        ),
        migrations.AddField(
            model_name='usertopic',
            name='Topic_fk',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='topic.topiccomponent'),
            preserve_default=False,
        ),
    ]
