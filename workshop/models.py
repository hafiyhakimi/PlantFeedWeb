from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed

from member.models import Person

# Create your models here.

class Workshop(models.Model):
    class Meta:
        db_table = 'Workshop'
    ProgrammeName = models.CharField(max_length=150,default="")
    Description=models.CharField(max_length=150,default="")
    Date = models.CharField(max_length=150,blank=True, null=True)
    Session = models.CharField(max_length=150)

    def save(self):
        super().save()


class Booking(models.Model):
    class Meta:
        db_table = 'Booking'
    ProgrammeName = models.CharField(max_length=150,default="",null=True)
    Date = models.CharField(max_length=150,blank=True, null=True)
    Session = models.CharField(max_length=150,null=True)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)

    def save(self):
        super().save()

