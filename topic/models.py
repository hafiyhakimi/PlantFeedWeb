from django.db import models

from member.models import Person
    
class TopicComponent(models.Model):
    class Meta:
        db_table = 'TopicComponent'
    TopicName = models.CharField(max_length=150)
    Status = models.CharField(max_length=100, default="Suggested")
    
class UserTopic(models.Model):
    class Meta:
        db_table = 'UserTopic'
    Topic_fk = models.ForeignKey(TopicComponent, on_delete=models.CASCADE)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)
    
class TopicComposite(TopicComponent):
    @staticmethod
    def get_topics(status):
        query = TopicComponent.objects.all()
        if status:
            query = query.filter(Status=status)
        return query
    
    @staticmethod
    def approve_topic(topic_name):
        query = TopicComponent.objects.filter(TopicName=topic_name).update(Status="Approved")
        return query
    
    @staticmethod
    def reject_topic(topic_name):
        query = TopicComponent.objects.filter(TopicName=topic_name).update(Status="Rejected")
        return query
        
    @staticmethod
    def add_topic(topic_name):
        TopicComponent.objects.create(TopicName=topic_name, Status="Approved")
        return True
    
    @staticmethod
    def delete_topic(topic_name):
        TopicComponent.objects.filter(TopicName=topic_name).delete()
        return True
        