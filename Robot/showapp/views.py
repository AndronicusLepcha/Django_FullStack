from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello This is Index")
def robot(request):
    text_dict={'insert_me':"Hello this is from showapp/views.py"}
    return render(request,'showapp/index.html',context=text_dict)