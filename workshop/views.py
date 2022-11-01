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
from workshop.models import Workshop
from member.models import Person


# Create your views here.

#workshop
def workshop(request):
        try:
            data=Workshop.objects.all()
            return render(request,'workshop.html',{'data':data})
        except Workshop.DoesNotExist:
            raise Http404('Data does not exist')
            
def createWorkshop(request):
    if request.method=='POST':
        ProgrammeName=request.POST.get('ProgrammeName')
        Description=request.POST.get('Description')
        Date=request.POST.get('Date')
        Session=request.POST.get('Session')
        Workshop(ProgrammeName=ProgrammeName,Description=Description,Date=Date,Session=Session).save(),
        messages.success(request,'The ' + request.POST['ProgrammeName'] + " is save succesfully..!")
        return render(request,'CreateWorkshop.html')
    else :
        return render(request,'CreateWorkshop.html')

def booking(request):
    #person = Person.objects.filter(Email=request.session['Email'])
    #return render(request, 'booking.html',{'person': person})

    #try:
    #    data=Workshop.objects.all() #filter(ProgrammeName=request.session['ProgrammeName'])
    #    return render(request,'booking.html',{'data':data})
    #except Workshop.DoesNotExist:
    #    raise Http404('Data does not exist')

    if request.method=='POST':
        ProgrammeName=request.POST.get('ProgrammeName')
        Date=request.POST.get('Date')
        Session=request.POST.get('Session')
        Workshop(ProgrammeName=ProgrammeName,Date=Date,Session=Session).save(),
        messages.success(request,'The booking of ' + request.POST['ProgrammeName'] + " is save succesfully..!")
        return render(request,'booking.html')

    else:
        return render(request,'booking.html')

    #data = Workshop.objects.all#filter(ProgrammeName=request.session['ProgrammeName'])
    #return render(request, 'booking.html',{'data': data})


