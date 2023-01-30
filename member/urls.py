
from django.urls import path
from django.urls import re_path as url, include

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import authentication
from rest_framework_simplejwt.views import TokenRefreshView

from group.views import updateGroup

from rest_framework.authtoken.views import obtain_auth_token
from member.api import UserAuthentication, UserList
from .import views
from .import api


urlpatterns = [
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
    
    path('MainMarketplace.html',views.mainMarketplace, name="MainMarketplace"),
    path('SellProduct.html/<str:fk1>/',views.sellProduct, name="SellProduct"),
    path('DeleteProduct/<str:fk1>/',views.deleteProduct, name="DeleteProduct"),
    path('UpdateProduct.html/<str:fk1>/',views.updateProduct, name="UpdateProduct"),
    
    path('buy_now/<str:fk1>/<str:fk2>/',views.buy_now, name='buy_now'),
    path('add_to_basket/<str:fk1>/<str:fk2>/',views.add_to_basket, name='add_to_basket'),
    # path('summary/', views.basket_summary, name='basket_summary'),
    
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
    
    # path('Payment.html', views.BasketView, name='basket'),
    
    path('pay', views.pay, name='pay'),
    
    # path('orderplaced/', views.order_placed, name='order_placed'),
    # path('error/', views.Error.as_view(), name='error'),
    # path('webhook/', views.stripe_webhook),

    # path('summary_view.html', views.basket_summary, name='basket_summary'),
    path('summary.html', views.summary, name='summary'),
    path('history.html', views.history, name='history'),
    path('invoice.html/<str:fk1>/', views.invoice, name='invoice'),
    path('remove_basket_qty/', views.remove_basket_qty, name='remove_basket_qty'),
    path('add_basket_qty/', views.add_basket_qty, name='add_basket_qty'),
    # path('add/', views.basket_add, name='basket_add'),
    path('basket_delete/', views.basket_delete, name='basket_delete'),
    # path('update/', views.basket_update, name='basket_update'),
    
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







