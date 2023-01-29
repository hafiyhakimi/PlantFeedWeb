from django.db import models

from member.models import Person

class Topic(models.Model):
    class Meta:
        db_table = 'Topic'
    TopicName = models.CharField(max_length=150)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)

class ApprovedTopic(models.Model):
    class Meta:
        db_table = 'approvedTopic'
    TopicName = models.CharField(max_length=150)

class SuggestedTopic(models.Model):
    class Meta:
        db_table = 'suggestedTopic'
    TopicName = models.CharField(max_length=150)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)

# Create your models here.
