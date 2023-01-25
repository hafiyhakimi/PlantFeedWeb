from django.db import models, migrations
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save
from member.models import Person
from sharing.models import Feed
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your models here.

class GroupMemberFactory:
    def create_group_member(self, userlevel):
        if userlevel == 1:
            return AdminGroupMember()
        else:
            return NormalGroupMember()

class GroupMember:
    def __init__(self):
        self.factory = GroupMemberFactory()

    def create_member(self, userlevel):
        self.member = self.factory.create_group_member(userlevel)
        return self.member
    
class NormalGroupMember:
    def updateMemberGroupSharing(request, fk2):
        sharing = GroupSharing.objects.get(id=fk2)
        person = Person.objects.filter(Email=request.session['Email'])
        groupmember = GroupMember.objects.filter(Person_fk=person)
        if sharing.Person_fk == person or groupmember.Userlevel == 1:
            if request.method == 'POST':
                sharing.GTitle = request.POST.get('GTitle')
                sharing.GMessage = request.POST.get('GMessage')
                sharing.GPhoto = request.POST.get('GPhoto')
                sharing.GVideo = request.POST.get('GVideo')
                sharing.save()
                messages.success(request, 'Sharing has been updated successfully!')
                return redirect('homepage')
            else:
                return render(request, 'EditGroupSharing.html', {'sharing': sharing, 'person':person})
        else:
            messages.error(request, 'You are not authorized to delete this sharing!')
            return redirect('homepage')

    def deleteMemberGroupSharing(request, fk2):
        sharing = GroupSharing.objects.get(id=fk2)
        person = Person.objects.filter(Email=request.session['Email'])
        groupmember = GroupMember.objects.filter(Person_fk=person)
        if sharing.Person_fk == person or groupmember.Userlevel == 1:
            if request.method == 'POST':
                sharing.delete()
                messages.success(request, 'Sharing has been deleted successfully!')
                return redirect('homepage')
            else:
                return render(request, 'DeleteGroupSharing.html', {'sharing': sharing, 'person':person})
        else:
            messages.error(request, 'You are not authorized to delete this sharing!')
            return redirect('homepage')

class AdminGroupMember:
    def updateAdminGroupSharing(request, fk2):
        sharing = GroupSharing.objects.get(id=fk2)
        person = Person.objects.filter(Email=request.session['Email'])
        # Check if the user is an admin
        member = GroupMember.objects.get(Person_fk=person)
        if member.Userlevel == 1:
            if request.method == 'POST':
                sharing.GTitle = request.POST.get('GTitle')
                sharing.GMessage = request.POST.get('GMessage')
                sharing.GPhoto = request.POST.get('GPhoto')
                sharing.GVideo = request.POST.get('GVideo')
                sharing.save()
                messages.success(request, 'Sharing has been updated successfully!')
                return redirect('homepage')
            else:
                return render(request, 'update_sharing.html', {'sharing': sharing, 'person':person})
        else:
            messages.error(request, 'You are not authorized to update this sharing')
            return redirect('homepage')
        
    def deleteAdminGroupSharing(request, fk2):
        sharing = GroupSharing.objects.get(id=fk2)
        person = Person.objects.filter(Email=request.session['Email'])
        # Check if the user is an admin
        member = GroupMember.objects.get(Person_fk=person)
        if member.Userlevel == 1:
            if request.method == 'POST':
                sharing.delete()
                messages.success(request, 'Sharing has been deleted successfully!')
                return redirect('homepage')
            else:
                return render(request, 'delete_sharing.html', {'sharing': sharing, 'person':person})
        else:
            messages.error(request, 'You are not authorized to delete this sharing')
            return redirect('homepage')
    
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

class GroupMember(models.Model):
    class Meta:
        db_table = 'GroupMember'
    Username = models.CharField(max_length=150, null=True)
    Userlevel = models.IntegerField(null=True)
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
    Group_fk = models.ForeignKey(Group, on_delete=models.CASCADE)
    Person_fk = models.ForeignKey(Person, on_delete=models.CASCADE)
    # Member_fk = models.ForeignKey(GroupMember, on_delete=models.CASCADE)

    def save(self):
        super().save()
    

    
