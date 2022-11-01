from django.contrib import admin
from django.urls import path
#from django.conf.urls import include
#from LOGIN import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from LOGIN.views import UserReg, sharing, discussion, view, workshop, booking, member
from .import views
from django.conf.urls import url
# from .import index

#from .api import UserList, UserDetail, UserAuthentication

urlpatterns = [
    path('MainGroup.html', views.mainGroup, name="MainGroup"),
    path('group.html', views.group, name="Group"),
    path('MyGroup.html',views.myGroup, name="MyGroup"),
    path('CreategroupAdmin.html',views.GroupAdmin, name="GroupAdmin"),
    path('EditGroup.html',views.updateGroup, name="updateGroup"),
 

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







