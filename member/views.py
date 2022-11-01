from datetime import time
from io import StringIO
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404, resolve_url
# from django.shortcuts import pyrebase
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django import forms
#from firebase_admin import firestore
#from firebase_admin.auth import UidIdentifier, UserIdentifier
#from pyasn1_modules.rfc2459 import UserNotice
#from pyrebase.pyrebase import Database
#from rest_framework import authentication, serializers
#from rest_framework.permissions import AllowAny
# from .forms import CreateInDiscussion, PersonForm, UserUpdateForm
#from rest_framework.parsers import JSONParser
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.db.models.signals import post_save
from django.dispatch import receiver
from cryptography.fernet import Fernet
from workshop.models import Booking, Workshop
from group.models import Group, GroupMember, GroupSharing
from .models import Person
from member.models import Member
from sharing.models import Feed
from rest_framework.permissions import AllowAny
from member.serializers import MyTokenObtainPairSerializer, UsersSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import requests
#from member.models import Users 
from .serializers import UsersSerializer
import pyrebase 
from django.contrib import auth
from getpass import getpass
from rest_framework import viewsets
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from member import serializers

cred = credentials.Certificate('member\serviceAccountKey.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

firebaseConfig={

    "apiKey": "AIzaSyDHx0RR2nsDiJECbaP4DpLpejjqutLPN34",
    "authDomain": "i-grow-kmma.firebaseapp.com",
    "projectId": "i-grow-kmma",
    "databaseURL": "xxxxxxxx",
    "storageBucket": "i-grow-kmma.appspot.com",
    "messagingSenderId": "426593032564",
    "appId": "1:426593032564:web:37f2948f17ae0cde6fb421",
    "measurementId": "G-Z1JJD88MCZ"
}

firebase = pyrebase.initialize_app(firebaseConfig)

authe = firebase.auth()
database=firebase.database()
 
def encryptPassword(Pwd):
         key = Fernet.generate_key()
         fernet = Fernet(key)
         encrypted = fernet.encrypt(Pwd.encode())
         return encrypted

def deryptPassword(Pwd):
         key = Fernet.generate_key()
         fernet = Fernet(key)
         decrypted = fernet.decrypt(Pwd).decode()
         return decrypted







def signIn(request):
    if request.method=='POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = authe.sign_in_with_email_and_password(email,password)
        except:
            message="Invalid Credentials"
            return render(request, 'signIn.html', {"mssg":message})
        print(user['idToken'])
        session_id=user['idToken']
        request.session['uid']=str(session_id)
        return render(request, 'signIn.html')
    
    else:
        return render(request,'signIn.html')

def signUp(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username=request.POST.get('username')
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        district=request.POST.get('district')
        state=request.POST.get('state')
        occupation=request.POST.get('occupation')
        about=request.POST.get('about')
        gender=request.POST.get('gender')
        maritalstatus=request.POST.get('maritalstatus')
        userlevel = request.POST.get('userlevel')
        Photo = request.POST.get('Photo')
        #resume = request.POST.get('resume')
        # Person(Email=Email,Password=Pwd,Username=Username,Name=Name,DateOfBirth=DateOfBirth,Age=Age,District=District,State=State,
        #     Occupation=Occupation,About=About,Gender=Gen,MaritalStatus=MaritalStatus,UserLevel=UserLevel,Photo=Photo).save(),

        try: 
            user=authe.create_user_with_email_and_password(email,password)
        except:
            message="Unable to create a new user. Please try again"
            return render(request,'registration.html', {"mssg":message})
        
        data={
            u'username': username,
            u'name': name, 
            u'dob': dob, 
            u'age': age, 
            u'district': district, 
            u'state': state, 
            u'occupation': occupation,
            u'about': about, 
            u'gender': gender, 
            u'maritalstatus': maritalstatus, 
            u'userlevel': userlevel,
            }

        db.collection(u'person').document().set(data)
        return render(request,'signIn.html')
    else :
        return render(request,'registration.html')



def postsign(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    login = auth.sign_in_with_email_and_password(email,password)
    return render(request, 'postsign.html')

def user_list(request):

    if request.method == 'GET':
        person = Person.objects.all()
        serializer = UsersSerializer(person, many=True)
        return JsonResponse(serializers.data, safe=False)

    else:
        request.method == 'POST'
        data = JSONParser().parse(request)
        serializer = UsersSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status = 201)
        return JsonResponse(serializer.errors, status=400)




def Indexpage(request):
    return render(request, 'index.html')

def homepage(request):
    person = Person.objects.filter(Email=request.session['Email'])
    
    return render(request, 'homepage.html',{'person': person })

def homepageAdmin(request):
    person = Person.objects.filter(Email=request.session['Email'])
    return render(request, 'homepageAdmin.html',{'person': person })


#user registration
def UserReg(request):
    if request.method=='POST':
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        Username=request.POST.get('username')
        Name=request.POST.get('name')
        DateOfBirth=request.POST.get('dob')
        Age=request.POST.get('age')
        District=request.POST.get('district')
        State=request.POST.get('state')
        Occupation=request.POST.get('occupation')
        About=request.POST.get('about')
        Gender=request.POST.get('gender')
        MaritalStatus=request.POST.get('maritalstatus')
        UserLevel = request.POST.get('userlevel')
        Photo = request.POST.get('Photo')
        #resume = request.POST.get('resume')
        Person(Email=Email,Password=Password,Username=Username,Name=Name,DateOfBirth=DateOfBirth,Age=Age,District=District,State=State,
            Occupation=Occupation,About=About,Gender=Gender,MaritalStatus=MaritalStatus,UserLevel=UserLevel,Photo=Photo).save(),

        #try: 
        #    user=authe.create_user_with_email_and_password(email,password)
        #except:
        #    message="Unable to create a new user. Please try again"
        #    return render(request,'registration.html', {"mssg":message})
        #uid=user['localId']
        
        #data={username: "username", name:"name", dob:"dob", age:"age", district:"district", state:"state", occupation:"occupation",about:"about", gender:"gender", maritalstatus:"maritalstatus", userlevel:"userlevel"}
        #Database.child("person").child(uid).child("details").set(data)

        #ranking = request.POST.get('ranking')
        
        #Users(Person, ranking=ranking)
        #Users.upload_photo(Person, photo)
        #Users.upload_file(Person, resume)

        #cuba
        # FarmingPerson(Email=Email,Password=Pwd,Username=Username,Name=Name,DateOfBirth=DateOfBirth,Age=Age,District=District,State=State,
        #     Occupation=Occupation,About=About,Gender=Gen,MaritalStatus=MaritalStatus).save(),
        # FarmingPerson(Email=Email,Password=Pwd,Username=Username,Name=Name,DateOfBirth=DateOfBirth,Age=Age,District=District,State=State,
            # Occupation=Occupation,About=About,Gender=Gen,MaritalStatus=MaritalStatus),
        #messages.success(request,'The new user ' + request.POST['Email'] + " is save succesfully..!")
        return render(request,'registration.html')
    else :
        return render(request,'registration.html')



#user login
def loginpage(request):
    if request.method == "POST":
        try:
            #UserLevel = Person.objects.get(Userlevel = request.POST['UserLevel'])
            Userdetails = Person.objects.get(Email = request.POST['Email'], Password = (request.POST['Pwd']))
            UserLevel = (request.POST.get('UserLevel'))
            print("Username", Userdetails)
            request.session['Email'] = Userdetails.Email
            person = Person.objects.filter(Email = request.POST['Email'])
            request.session['UserLevel'] = Userdetails.UserLevel
            if request.session['UserLevel'] == 'user':
            #user = Person.objects.filter(UserLevel = request.Post['UserLevel'])
                return render(request,'homepage.html',{'person' : person})
            else:
                return render(request,'homepageAdmin.html',{'person' : person})
        except Person.DoesNotExist as e:
            messages.success(request,'Username/Password Invalid..!')
    return render(request,'login.html')

#user logout
def logout(request):
    #try:
    #    del request.session['Email']
    #except:
    #    return render(request,'index.html')
    auth.logout(request)
    return render(request,'index.html')

#profile
def view(request):
    person = Person.objects.filter(Email=request.session['Email'])
    if request.method=='POST':
       t = Person.objects.get(Email=request.session['Email'])
       t.Password=request.POST['Password']
       t.Username=request.POST.get('Username')
       t.Name=request.POST.get('Name')
       t.DateOfBirth=request.POST.get('DateOfBirth')
       t.Age=request.POST['Age']
       t.District=request.POST['District']
       t.State=request.POST['State']
       t.Occupation=request.POST['Occupation']
       t.About=request.POST['About']
       t.Gen=request.POST.get('Gender')
       t.MaritalStatus=request.POST.get('MaritalStatus')
       t.photo=request.POST.get('photo')
       t.save()

       return render(request,'homepage.html')
    else:
        return render(request, 'profile.html',{'person': person})  

#list of user for admin view
def UserList(request):
    person = Person.objects.all()
    return render(request, 'UserList.html',{'person': person})  

#sharing
def mainSharing(request):
    try:
        feed=Feed.objects.all()
        person = Person.objects.filter(Email=request.session['Email'])
        user=Person.objects.all()
        sharing = GroupSharing.objects.all()
        return render(request,'MainSharing.html',{'feed':feed, 'person':person, 'user':user, 'sharing':sharing})
    except Feed.DoesNotExist:
        raise Http404('Data does not exist')

def sharing(request, fk1):
    person = Person.objects.get(pk=fk1)
    if request.method=='POST':
        Title=request.POST.get('Title')
        Message=request.POST.get('Message')
        Photo=request.POST.get('Photo')
        Video=request.POST.get('Video')
        f = Person.objects.get(pk=fk1)
        #Graph=request.POST.get('Graph')
        Feed(Title=Title,Message=Message,Photo=Photo,Video=Video,Person_fk=f).save(),
        messages.success(request,'The new feed is save succesfully..!')

        #data={
        #    u'title': Title,
        #    u'message':Message,
        #    u'photo':Photo,
        #    u'video':Video,

        #}
        #db.collection(u'sharing').document().set(data)
        return render(request,'sharing.html',{'person':person})
    else :
        return render(request,'sharing.html')

def viewSharing(request):
    feed = Feed.objects.all()
    sharing = GroupSharing.objects.all()
    person = Person.objects.filter(Email=request.session['Email'])
    return render(request,'ViewSharing.html',{'feed':feed, 'person':person, 'sharing':sharing})  

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
       return redirect('../../MainSharing.html')
       
    else:
        return render(request,'ViewSharing.html',{'feed':feed})

def deleteSharing(request,fk1):
    feed = Feed.objects.get(pk=fk1)
    if request.method=='POST':
        feed.delete()
        return redirect('../../Home')
    context = {
        "object" : feed
    }
    return render(request, 'deleteSharing.html', {'object':feed})

    #feed_id = int(feed_id)
    #try:
    #    feed_sel = Feed.objects.get(id = feed_id)
    #except Feed.DoesNotExist:
    #    return redirect('index')
    #feed_sel.delete()
    #return redirect('index')





#group
def mainGroup(request):
    try:
        group=Group.objects.all()
        person = Person.objects.all()
        user = Person.objects.filter(Email=request.session['Email'])
        member = GroupMember.objects.all()

        #feed = Feed.objects.all()
        return render(request,'MainGroup.html',{'group':group, 'person':person, 'user':user, 'member':member})
    except Group.DoesNotExist:
        raise Http404('Data does not exist')

def GroupAdmin(request):
    try:
        group=Group.objects.all()
        return render(request,'CreategroupAdmin.html',{'group':group})
    except Group.DoesNotExist:
        raise Http404('Data does not exist')

def group(request, fk1):
    #person_fk = Person.objects.filter()
    group=Group.objects.all()
    user = Person.objects.filter(Email=request.session['Email'])
    person = Person.objects.get(pk=fk1)
    if request.method=='POST':
        p = Person.objects.get(pk=fk1)
        GName=request.POST.get('GName')
        GAbout=request.POST.get('GAbout')
        GProfile=request.POST.get('GProfile')
        GMedia=request.POST.get('GMedia')
        Group(GName=GName,GAbout=GAbout,GMedia=GMedia, GProfile=GProfile, Person_fk=p).save(),
        messages='The new group ' + request.POST['GName'] + ' is create succesfully..! Be the admin of the group?'
        return render(request,'MainGroup.html',{'mssg':messages,'group':group, 'user':user})

    else :
        return render(request,'group.html')

def myGroup(request):
    try:
        group = Group.objects.all()
        Gmember = GroupMember.objects.all()
        return render(request,'MyGroup.html',{'group':group, 'Gmember':Gmember})
    except Group.DoesNotExist:
       raise Http404('Data does not exist')

def updateGroup(request, fk1, fk):
    #group = Group.objects.filter(Name=request.session['GName'])
    user = Person.objects.filter(Email=request.session['Email'])
    g = Group.objects.get(pk=fk1)
    person = Person.objects.filter(Email=request.session['Email'])
    gmember = GroupMember.objects.all()
    group = Group.objects.all()
    if request.method=='POST':
        t = Group.objects.get(pk=fk1)
        f = Person.objects.get(pk=fk)
        #GUsername = request.POST.get('Username')
        GroupMember(Username=f.Username, Group_fk=t, Person_fk=f).save(),
        messages="Your username is successfully added"
        return redirect('../../../MainGroup.html', {'group':group, 'person':person, 'gmember':gmember,'user':user, 'g':g})

    else:
        return render(request, 'EditGroup.html', {'group':group, 'person':person, 'user':user, 'g':g})

def GSharing(request, fk1,fk3):
    group = Group.objects.get(pk=fk3)
    person = Person.objects.filter(Email=request.session['Email'])
    sharing = GroupSharing.objects.all()
    user = Person.objects.all()
    gr = Group.objects.all()
    if request.method=='POST':
        p = Person.objects.get(pk=fk1)
        g = Group.objects.get(pk=fk3)
        GTitle=request.POST.get('GTitle')
        GMessage=request.POST.get('GMessage')
        GPhoto=request.POST.get('GPhoto')
        GVideo=request.POST.get('GVideo')
        
        GroupSharing(GTitle=GTitle,GMessage=GMessage,GPhoto=GPhoto,GVideo=GVideo,Person_fk=p, Group_fk=g).save(),
        messages='The new feed' + request.POST['GTitle'] + "is save succesfully..!"
        return render(request,'homepage.html',{'group':gr, 'person':user, 'user':person, "mssgs":messages})
    else :
        return render(request,'AddGroupSharing.html',{'group':group, 'person':person, 'sharing':sharing})

def AddGroupSharing(request, fk1):
    try:
        group = Group.objects.get(pk=fk1)
        person = Person.objects.filter(Email=request.session['Email'])
        #Gsharing = GroupSharing.objects.all()
        sharing = GroupSharing.objects.all()
        return render(request,'AddGroupSharing.html',{'group':group, 'person':person, 'sharing':sharing})
    except Group.DoesNotExist:
        raise Http404('Data does not exist')

def ViewGroupSharing(request, fk1):
    try:
        group = Group.objects.get(pk=fk1)
        g = Group.objects.all()
        sharing = GroupSharing.objects.all()
        person = Person.objects.filter(Email=request.session['Email'])
        user = Person.objects.all()
        member = GroupMember.objects.all()
        return render(request,'ViewGroupSharing.html',{'group':group, 'g':g,'person':person,'sharing':sharing, 'member':member,'user':user})  
    except Group.DoesNotExist:
        raise Http404('Data does not exist')

def deleteGroupSharing(request,fk1):
    gsharing = GroupSharing.objects.get(pk=fk1)
    if request.method=='POST':
        gsharing.delete()
        message='Group sharing is successfully deleted'
        return redirect('../../Home',{'mssg':message})
    context = {
        "object" : workshop
    }
    return render(request, 'deleteGroupSharing.html', {'object':gsharing})

def updateGroupSharing(request, fk1):
    sharing = GroupSharing.objects.get(pk=fk1)
    if request.method=='POST':
       f = sharing = GroupSharing.objects.get(pk=fk1)
       f.GTitle=request.POST['GTitle']
       f.GMessage=request.POST.get('GMessage')
       f.GPhoto=request.POST.get('GPhoto')
       f.GVideo=request.POST.get('GVideo')
       #f.Graph=request.POST['Graph']
       f.save()
       return redirect('../../MainGroup.html')
       
    else:
        return render(request,'EditGroupSharing.html',{'sharing':sharing})





#member
def mainMember(request):
    try:
        member = Member.objects.all()
        return render(request,'MainMember.html',{'member':member})
    except Member.DoesNotExist:
        raise Http404('Data does not exist')

def member(request):
    if request.method=='POST':
        Name=request.POST.get('Name')
        Study=request.POST.get('Study')
        Lives=request.POST.get('Lives')
        Member(Name=Name,Study=Study,Lives=Lives).save(),
        messages.success(request,'The new member ' + request.POST['Name'] + " is create succesfully..!")
        return render(request,'member.html')
    else :
        return render(request,'member.html')
def friendlist(request):
    #try:
    #    member=Member.objects.filter(Name=request.session['Name'])
        return render(request,'friendlist.html')#{'member':member})
    #except Member.DoesNotExist:
     #   raise Http404('Data does not exist')


def myMember(request):
    #try:
    #    member=Member.objects.filter(Name=request.session['Name'])
        return render(request,'MyMember.html')#{'member':member})
    #except Member.DoesNotExist:
     #   raise Http404('Data does not exist')

def MainSearchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        Name = Person.objects.all().filter(Name=search)
        return render(request, 'MainSearchbar.html', {'Name': Name})




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





#workshop
def workshop(request):
        try:
            data=Workshop.objects.all()
            person = Person.objects.filter(Email=request.session['Email'])
            return render(request,'workshop.html',{'data':data, 'person':person})
        except Workshop.DoesNotExist:
            raise Http404('Data does not exist')

def BookWorkshop(request):
        try:
            data=Workshop.objects.all()
            person = Person.objects.filter(Email=request.session['Email'])
            return render(request,'BookWorkshop.html',{'data':data,'person':person})
        except Workshop.DoesNotExist:
            raise Http404('Data does not exist') 

def BookingList(request):
        try:
            data=Workshop.objects.all()
            booking = Booking.objects.all()
            person = Person.objects.filter(Email=request.session['Email'])
            return render(request,'BookingList.html',{'data':data,'person':person,'booking':booking})
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

def booking(request, fk1):
    #person = Person.objects.filter(Email=request.session['Email'])
    #return render(request, 'booking.html',{'person': person})

    #try:
    #    data=Workshop.objects.all() #filter(ProgrammeName=request.session['ProgrammeName'])
    #    return render(request,'booking.html',{'data':data})
    #except Workshop.DoesNotExist:
    #    raise Http404('Data does not exist')
    person = Person.objects.get(pk=fk1)
    data=Workshop.objects.all()
    booking=Booking.objects.all()
    p1 = Person.objects.filter(Email=request.session['Email'])
    if request.method=='POST':
        p = Person.objects.get(pk=fk1)
        ProgrammeName=request.POST.get('ProgrammeName')
        Date=request.POST.get('Date')
        Session=request.POST.get('Session')
        Booking(ProgrammeName=ProgrammeName,Date=Date,Session=Session, Person_fk=p).save(),
        message="The booking of is save succesfully..!"
        return render(request,'BookWorkshop.html',{'data':data, 'p1':p1,'booking':booking, "mssg":message})
    else :
       return render(request,'BookWorkshop.html',{'data':data, 'p1':p1, 'booking':booking})

    #data = Workshop.objects.all#filter(ProgrammeName=request.session['ProgrammeName'])
    #return render(request, 'booking.html',{'data': data})

#class Users(viewsets.ModelViewSet):
#    queryset = Users.objects.all() 
#    serializer_class = UsersSerializer

def deleteWorkshop(request,fk1):
    workshop = Workshop.objects.get(pk=fk1)
    if request.method=='POST':
        workshop.delete()
        return redirect('../../HomeAdmin')
    context = {
        "object" : workshop
    }
    return render(request, 'deleteSharing.html', {'object':workshop})

def deleteBooking(request,fk1):
    booking = Booking.objects.get(pk=fk1)
    if request.method=='POST':
        booking.delete()
        message="The booking of is save succesfully..!"
        return redirect('../../BookingList.html', {"mssg":message})
    context = {
        "object" : booking
    }
    return render(request, 'deleteBooking.html', {'object':booking})

#class MyObtainTokenPairView(TokenObtainPairView):
 #   permission_classes = (AllowAny,)
    #authentication_class = 
  #  Email = serializers.CharField(required=False)
   # username = Email
    #serializers_class = MyTokenObtainPairSerializer
    #def get_token(cls, user):
    #        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
     #       token['username'] = user.Email
      #      return token


