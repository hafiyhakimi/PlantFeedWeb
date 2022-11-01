from django.contrib import admin
from django.contrib.auth.models import Group

from member.views import group, workshop
from .models import Person
from .models import Feed
from group.models import Group
from .models import Member
#from .models import Booking
from workshop.models import Workshop
from .models import SensorData
from .models import Plants
# from .models import Comment
from .models import *

admin.site.register(Person)
admin.site.register(Member)
admin.site.register(SensorData)
admin.site.register(Plants)

# Register your models here.
#admin.site.register(Person)
#admin.site.register(Group)
#admin.site.register(Workshop)
#admin.site.register(Feed)

