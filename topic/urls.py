from django.contrib import admin
from django.urls import path
from django.urls import re_path as url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .import views

urlpatterns = [
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()







