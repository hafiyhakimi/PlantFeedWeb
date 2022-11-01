from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
# from LOGIN.models import Person as FarmingPerson
# from LOGIN.models import Feed, Booking, Workshop, Group, Member 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
# from .forms import CreateInDiscussion, PersonForm, UserUpdateForm
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_save
from django.dispatch import receiver
from cryptography.fernet import Fernet
from member.models import Person
from sharing.models import Feed
# from .models import Person

# Create your views here.


#sharing
def mainSharing(request):
    try:
        feed=Feed.objects.all()
        return render(request,'MainSharing.html',{'feed':feed})
    except Feed.DoesNotExist:
        raise Http404('Data does not exist')

def sharing(request):
    if request.method=='POST':
        Title=request.POST.get('Title')
        Message=request.POST.get('Message')
        Photo=request.POST.get('Photo')
        Video=request.POST.get('Video')
        #person = Person.objects.filter(Email=request.session['id'])
        #Graph=request.POST.get('Graph')
        Feed(Title=Title,Message=Message,Photo=Photo,Video=Video).save(),
        messages.success(request,'The new feed is save succesfully..!')

        #data={
        #    u'title': Title,
        #    u'message':Message,
        #    u'photo':Photo,
        #    u'video':Video,

        #}
        #db.collection(u'sharing').document().set(data)
        return render(request,'sharing.html')
    else :
        return render(request,'sharing.html')


#def viewSharing(request):
    #feed = Feed.objects.all()
    #return render(request,'ViewSharing.html',{'feed':feed})  

def updateSharing(request, fk1):
    feed = Feed.objects.get(pk=fk1)
    if request.method=='POST':
       f = feed = Feed.objects.get(pk=fk1)
       f.Title=request.POST['Title']
       f.Message=request.POST.get('Message')
       f.Photo=request.POST.get('Photo')
       f.Video=request.POST.get('Video')
       #f.Graph=request.POST['Graph']
       f.save()
       return render(request,'ViewSharing.html',{'feed':feed})
    else:
        return render(request, 'homepage.html', {'feed':feed})

def deleteSharing(request,id):
    sharing = get_object_or_404(sharing, id=id)
    if request.method=='POST':
        sharing.delete()
        return redirect('homepage.html')
    context = {
        "object" : sharing
    }
    return render(request, 'deleteSharing.html', {'object':sharing})

    #feed_id = int(feed_id)
    #try:
    #    feed_sel = Feed.objects.get(id = feed_id)
    #except Feed.DoesNotExist:
    #    return redirect('index')
    #feed_sel.delete()
    #return redirect('index')


    #discussion
def viewdiscussion(request):
    if request.method=='POST':
        About=request.POST.get('About')
        Discussion=request.POST.get('Discussion')
        Media=request.POST.get('Media')
        Name=request.POST.get('Name')
        Discussion(About=About,Discussion=Discussion,Name=Name).save(),
        return render(request,'/home.html')
    else :
        return render(request,'discussion.html')

def discussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        context ={'form':form}
    return render(request,'group.html')
