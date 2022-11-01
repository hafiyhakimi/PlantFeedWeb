"""igrowKMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin, auth
from rest_framework.routers import DefaultRouter
from django.urls import path, include
#from .import views
from django.conf.urls import url, include
from rest_framework import authentication
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # path('',views.Indexpage),
    path('', include('member.urls')),
    path('', include('group.urls')),
    path('', include('sharing.urls')),
    path('', include('workshop.urls')),
    #path('auth/', include('auth.urls')),
    #path('api/', include('member.urls')),
]
