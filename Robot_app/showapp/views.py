from django.shortcuts import render
from django.http import HttpResponse
from showapp.models import Topic,Webpage,AccessRecord

def index(request):
    webpages=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages}
    return render(request,'showapp/index.html',context=date_dict)

def robot(request):
    text_dict={'insert_me':"Hello this is from showapp/views.py"}
    return render(request,'showapp/index.html',context=text_dict)