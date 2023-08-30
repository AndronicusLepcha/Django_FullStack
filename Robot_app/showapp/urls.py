from django.urls import path
from showapp import views
urlpatterns=[
    path('',views.robot,name='index'),
    #path('robot/',views.robot,name='robot')
]