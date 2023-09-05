from django.urls import path
from cr7 import views

urlpatterns=[
    path('',views.goat,name="realGoat"),
    path('addgoat/',views.Add,name="AddGoat")
]