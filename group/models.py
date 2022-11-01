from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from member.models import Person
from sharing.models import Feed
from django.shortcuts import render

# Create your models here.

class Group(models.Model):
    class Meta:
        db_table = 'Group'
    GName = models.CharField(max_length=150, null=True)
    GAbout = models.CharField(max_length=1000, null=True)
    GProfile = models.FileField(upload_to='media/',default="")
    GMedia = models.FileField(upload_to='media/',default="")
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)

    def save(self):
        super().save()
        super().save(using='farming')

class GroupMember(models.Model):
    class Meta:
        db_table = 'GroupMember'
    Username = models.CharField(max_length=150, null=True)
    Group_fk = models.ForeignKey(Group, on_delete=models.CASCADE)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)

    def save(self):
        super().save()
       

class GroupSharing(models.Model):
    class Meta:
        db_table = 'GroupSharing'
    GTitle = models.CharField(max_length=255, null=True, blank=True)
    GMessage = models.CharField(max_length=255, null=True, blank=True)
    GPhoto = models.ImageField(upload_to ='media/')
    GVideo = models.FileField(upload_to='videomedia/', null=True)
    #GGraph = models.FileField(upload_to='uploads/')
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)
    #Sharing_fk = models.ForeignKey(Feed, on_delete=models.CASCADE)
    Group_fk = models.ForeignKey(Group, on_delete=models.CASCADE)

    def save(self):
        super().save()
    

    
