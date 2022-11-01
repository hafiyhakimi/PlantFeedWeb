from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.syndication.views import Feed
from django.shortcuts import render
from group.models import Group

from member.models import Person

# Create your models here.


class Feed(models.Model):
    class Meta:
        db_table = 'Feed'
    Title = models.CharField(max_length=255, blank=True)
    Message = models.CharField(max_length=1500,blank=True)
    Photo = models.ImageField(upload_to ='images/')
    Video = models.FileField(upload_to='media/', null=True)
    Graph = models.FileField(upload_to='videomedia/')
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)

    def showvideo(request):

        lastvideo = video.objects.last()
        videofile = lastvideo.videofile
    
        form = SharingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

        context= {'videofile': videofile, 'form': form}

        return render(request, 'sharing.html', context)
    #def __str__(self):
       # return self.Message + ": " + str(self.videofile)

class Comment(models.Model):
    class Meta:
        db_table = 'Comment'    
    Message = models.CharField(max_length=255)
    Pictures = models.ImageField(upload_to='uploads/')
    Video = models.FileField(upload_to='uploads/')
