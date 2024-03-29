# Generated by Django 4.1.3 on 2023-02-08 15:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
        migrations.CreateModel(
            name='TopicComposite',
            fields=[
                ('topiccomponent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='topic.topiccomponent')),
            ],
            bases=('topic.topiccomponent',),
        ),
        migrations.CreateModel(
            name='UserTopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Person_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Topic_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.topiccomponent')),
            ],
            options={
                'db_table': 'UserTopic',
            },
        ),
    ]
