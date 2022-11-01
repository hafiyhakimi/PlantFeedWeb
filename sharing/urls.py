from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
# from LOGIN import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from LOGIN.views import UserReg, sharing, discussion, view, workshop, booking, member
from .import views
from django.conf.urls import url
# from .import index
# from .api import UserList, UserDetail, UserAuthentication

urlpatterns = [
    path('MainSharing.html',views.mainSharing, name="MainSharing"),
     path('sharing.html/<str:fk1>/',views.sharing, name="Sharing"),
    #path('ViewSharing',views.viewSharing,name="ViewSharing"),
    path('ViewSharing.html/<str:fk1>/',views.updateSharing, name="UpdateSharing"),
    path('deleteSharing.html', views.deleteSharing, name="DeleteSharing"),


] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







