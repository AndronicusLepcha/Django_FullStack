from django.conf.urls import url
from blog import views

urlpatterns=[
    path('about/',views.AboutView().as_view(),name='about'),
]