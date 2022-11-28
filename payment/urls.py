from django.urls import path
#from django.conf.urls import url
from . import views

app_name = 'payment'

urlpatterns = [
    path('Payment.html',views.payment, name="Payment"),
]