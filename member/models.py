from django import db
from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from ast import Pass
from django.db import models
from django.contrib.auth.models import User
#import firebase_admin
#from firebase_admin import credentials
#from firebase_admin import firestore

#cred = credentials.Certificate('D:\IGROW_V-main\member\serviceAccountKey.json')

#firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://i-grow-kmma.firebaseio.com'
#})


class Person(models.Model):
    Email = models.CharField(max_length=150, unique=True)
    # Pwd = models.CharField(max_length=150)
    Password = models.CharField(max_length=150)
    Username = models.CharField(max_length=150)
    Name = models.CharField(max_length=150)
    DateOfBirth = models.CharField(max_length=150)
    Age = models.IntegerField ()
    District = models.CharField(max_length=150)
    State = models.CharField(max_length=150)
    Occupation = models.CharField(max_length=150)
    About = models.CharField(max_length=150)
    Gender = models.CharField(max_length=1)
    MaritalStatus = models.CharField(max_length=150)
    UserLevel = models.CharField(max_length=10)
    Photo = models.ImageField(upload_to ='images/')
    #resume = models.ImageField(null=True, blank=True)

    @property
    def is_anonymous(self):
   
        return False
    @property
    def is_authenticated(self):
   
        return False

    def save(self):
        super().save()
        super().save(using='farming')

    class Meta:
        db_table = 'login_person'
        #db.collection('login_person')

        #fields = ['Email', 'Password']
    
    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['username']
        
def user_form(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)
        instance.Person.save()

class Member(models.Model):
    class Meta:
        db_table = 'Member'
    Name = models.CharField(max_length=150)
    Study = models.CharField(max_length=1000)
    Lives = models.CharField(max_length=1000)
    


class SensorData(models.Model):
    class Meta:
        db_table = 'SensorData'    
    Detail = models.CharField(max_length=255)
    Name = models.CharField(max_length=150)

class Plants(models.Model):
    class Meta:
        db_table = 'Plants'
    Pictures = models.ImageField(upload_to='uploads/')
    Species = models.CharField(max_length=150)
    Types = models.CharField(max_length=150)


class Users(models.Model):
    class Meta:
        db_table = 'Users'
    username = models.CharField(max_length=10, unique=True) #AI190201
    password = models.CharField(max_length=30) #ninja saga
    name = models.CharField(max_length=100) #FAIZ BIN AB. HAMID
    age = models.IntegerField() #22
    ranking = models.FloatField() #2.5

    def upload_photo(self, filename):
        path = 'member/photo/{}'.format(filename)
        return path

    photo = models.ImageField(upload_to=upload_photo, null=True, blank=True)

    def upload_file(self, filename):
        path = 'member/file/{}'.format(filename)
        return path

    resume = models.ImageField(upload_to=upload_file, null=True, blank=True)

    def __str__(self):
        return f"{self.Username} - {self.Password}"

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)