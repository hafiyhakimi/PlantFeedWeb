from django.contrib import admin
from django.urls import path
from django.urls import re_path as url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    
    path('selectTopic',views.selectTopic,name="selectTopic"),
    path('viewSelectedTopic',views.viewSelectedTopic,name="viewSelectedTopic"),
    path('updateSelectedTopic',views.updateSelectedTopic,name="updateSelectedTopic"),
    path('suggestNewTopic',views.suggestNewTopic,name="suggestNewTopic"),
    path('Managetopic', views.managetopic, name="Managetopic"),
 

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







