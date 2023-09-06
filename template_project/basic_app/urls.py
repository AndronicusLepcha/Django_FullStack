from django.urls import path,include
from . import views 

#template urls

app_name='basic_app' 

urlpatterns=[
    path('register/',views.register,name='register'),
    # path('other/',views.other,name='other'),
]