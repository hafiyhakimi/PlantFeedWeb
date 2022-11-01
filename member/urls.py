"""LOGIN URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
#from LOGIN import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import authentication
from rest_framework_simplejwt.views import TokenRefreshView

from group.views import updateGroup
#from .views import MyObtainTokenPairView, user_list
from rest_framework.authtoken.views import obtain_auth_token
from member.api import UserAuthentication, UserList
#from LOGIN.views import UserReg, sharing, discussion, view, workshop, booking, member
from .import views
from .import api
from django.conf.urls import url
# from .import index
#from member import views
#from rest_framework import routers

#router = routers.DefaultRouter(trailing_slash=False) 
#router.register('Userdetails', views.Users)


urlpatterns = [

    #url(r'^admin/', admin.site.urls),
    #url(r'^$',views.signIn, name="SignIn"),
    #url('sign',views.signUp),
    #path('registration.html',views.signUp, name="signUp"),
    url('^postsign/',views.postsign),
    path('',views.Indexpage),
    path('Home',views.homepage, name="Home"),
    path('HomeAdmin',views.homepageAdmin, name="HomeAdmin"),
    path('Registration', views.UserReg, name="Reg"),
    path('Loginpage', views.loginpage, name="Loginpage"),
    path('Logout',views.logout, name="Logout"),
    path('View',views.view,name="View"),

    path('MainSharing.html',views.mainSharing, name="MainSharing"),
    path('sharing.html/<str:fk1>/',views.sharing, name="Sharing"),
    #path('ViewSharing',views.viewSharing,name="ViewSharing"),
    path('ViewSharing.html/<str:fk1>/',views.updateSharing, name="UpdateSharing"),
    path('DeleteSharing.html/<str:fk1>/', views.deleteSharing, name="DeleteSharing"),

    path('MainGroup.html',views.mainGroup, name="MainGroup"),
    path('group.html/<str:fk1>/',views.group, name="Group"),
    path('MyGroup.html',views.myGroup, name="MyGroup"),
    path('CreategroupAdmin.html',views.GroupAdmin, name="GroupAdmin"),
    #path('CreategroupAdmin.html',views.GroupAdmin, name="GroupAdmin"),
    path('EditGroup.html/<str:fk1>/<str:fk>/',views.updateGroup, name="EditGroup"),
    #path('EditGroup.html',views.ViewEditGroup, name="ViewEditGroup"),
    #url(r'^world/(?P<world_pk>\d+)/(?P<country_pk>\d+)/$'
    
    path('AddGroupSharing.html/<str:fk1>/<str:fk3>/', views.GSharing, name="GSharing"),
    path('ViewGroupSharing.html/<str:fk1>/', views.ViewGroupSharing, name="ViewGroupSharing"),
    path('EditGroupSharing.html/<str:fk1>/',views.updateGroupSharing, name="UpdateGroupSharing"),
    path('DeleteGroupSharing.html/<str:fk1>/', views.deleteGroupSharing, name="DeleteGroupSharing"),
    

    path('MainMember.html', views.mainMember, name="MainMember"),
    path('member.html',views.member, name="member"),
    path('friendlist.html',views.friendlist, name="friendlist"),
    #path('MyMember.html',views.myMember, name="MyMember"),
    path('MainSearchbar', views.MainSearchbar, name='MainSearchbar'),
    path('UserList', views.UserList, name="UserList"),

    path('workshop.html',views.workshop, name="Workshop"),
    path('booking.html/<str:fk1>/',views.booking, name="Booking"),
    path('CreateWorkshop.html',views.createWorkshop, name="CreateWorkshop"),
    path('BookWorkshop.html',views.BookWorkshop, name="BookWorkshop"),
    path('BookingList.html',views.BookingList, name="BookingList"),
    path('deleteWorkshop.html/<str:fk1>/',views.deleteWorkshop, name="deleteWorkshop"),
    path('deleteBooking.html/<str:fk1>/',views.deleteBooking, name="deleteBooking"),

    url(r'^api/users_lists/$', UserList.as_view(), name='user_list'),
    #url(r'^api/users_list/(?P<id>\d+)/$', UserDetail.as_view(), name='user_list'),
    url(r'^api/auth/$', UserAuthentication.as_view(), name='User Authentication API'),
    #url(r'^rest-auth/', include('rest_auth.urls')),
    #url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
    #path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    #path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('userlist/', views.user_list, name='userlist'),
    #path('login', obtain_auth_token, name='login')
    path('users/login/', api.login_user, name='login'),
    path('users/token/<pk>', api.getUserFromToken, name='user-token'),
    

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







