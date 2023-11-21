from app1.views import *
from django.urls import path
app_name="goodthing"
urlpatterns=[
    path("call/",call,name="call")
]