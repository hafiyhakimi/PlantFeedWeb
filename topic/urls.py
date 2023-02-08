from django.urls import path

from . import views

app_name = 'topic'

urlpatterns = [
    path('selectTopic',views.selectTopic,name="selectTopic"),
    path('viewSelectedTopic',views.viewSelectedTopic,name="viewSelectedTopic"),
    path('updateSelectedTopic',views.updateSelectedTopic,name="updateSelectedTopic"),
    path('suggestNewTopic',views.suggestNewTopic,name="suggestNewTopic"),
    path('Managetopic', views.managetopic, name="Managetopic"),
    
]