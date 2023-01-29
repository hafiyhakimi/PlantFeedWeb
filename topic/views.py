from django.shortcuts import render
from django.contrib import messages

from topic.models import Topic, SuggestedTopic, ApprovedTopic
from member.models import Person


def selectTopic(request):
    if request.method == 'POST':
        person = Person.objects.get(Email=request.session['Email'])
        Topiclist = request.POST.getlist('topic')
        for topic in Topiclist:
            Topic.objects.create(TopicName=topic, Person_fk=person)
        return render(request, 'homepage.html')
    else:
        return render(request, 'Topic.html', {'person': person})

def viewSelectedTopic(request):
    person = Person.objects.filter(Email=request.session['Email'])
    personlist = Person.objects.filter(Email=request.session['Email'])[0]
    topics = Topic.objects.filter(Person_fk=personlist).values('TopicName').distinct()
    topic_list = ApprovedTopic.objects.values('TopicName').distinct()
    return render(request, 'viewTopic.html', {'person': person, 'topics': topics, 'topic_list': topic_list})

def updateSelectedTopic(request):
    if request.method == 'POST':
        person = Person.objects.filter(Email=request.session['Email'])
        personlist = Person.objects.filter(Email=request.session['Email'])[0]
        Topic.objects.filter(Person_fk=personlist).delete()
        Topiclist = request.POST.getlist('topic')
        for topic in Topiclist:
            Topic.objects.create(TopicName=topic, Person_fk=personlist)
        return render(request, 'profile.html',{'person': person})
    else:
        return render(request, 'Topic.html',{'person': person})

def suggestNewTopic(request):
    person = Person.objects.filter(Email=request.session['Email'])
    personlist = Person.objects.filter(Email=request.session['Email']).first()
    topics = Topic.objects.filter(Person_fk=personlist).values('TopicName').distinct()
    topic_list = ApprovedTopic.objects.values('TopicName').distinct()
    if request.method == 'POST':
        topicName = request.POST.get('topicsuggest')

        # Check if the topic already exists in the TopicList model
        topic_exists = ApprovedTopic.objects.filter(TopicName=topicName).exists()
        if topic_exists:
            messages.success(request,'Topic already exists..!')
            return render(request, 'viewTopic.html',{'person': person, 'topics': topics, 'topic_list': topic_list})

        # Create a new topic suggestion
        SuggestedTopic.objects.create(TopicName=topicName, Person_fk=personlist)
        return render(request, 'profile.html',{'person': person})
    else:
        return render(request, 'Topic.html',{'person': person})
    
def managetopic(request):
    person = Person.objects.filter(Email=request.session['Email'])
    suggestT = SuggestedTopic.objects.all()
    topics = ApprovedTopic.objects.all()
    if request.method == 'POST':
        stat = request.POST.get('status')
        topicName = request.POST.get('topicName')
            
        if stat == 'Approve':
            ApprovedTopic.objects.create(TopicName=topicName)
            SuggestedTopic.objects.filter(TopicName=topicName).delete()
            return render(request, 'ManageTopicAdmin.html',{'person': person , 'suggestT': suggestT, 'topics': topics})
        elif stat == 'Reject':
            SuggestedTopic.objects.filter(TopicName=topicName).delete()
            return render(request, 'ManageTopicAdmin.html',{'person': person , 'suggestT': suggestT, 'topics': topics})
        elif stat == 'Delete':
            ApprovedTopic.objects.filter(TopicName=topicName).delete()
            return render(request, 'ManageTopicAdmin.html',{'person': person , 'topics': topics, 'suggestT': suggestT})
        elif stat == 'Add':
            ApprovedTopic.objects.create(TopicName=topicName)
            return render(request, 'ManageTopicAdmin.html',{'person': person , 'topics': topics, 'suggestT': suggestT})
    return render(request, 'ManageTopicAdmin.html',{'person': person , 'suggestT': suggestT, 'topics': topics})

# Create your views here.
