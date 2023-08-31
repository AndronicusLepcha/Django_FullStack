from django.shortcuts import render
from django.http import HttpResponse
from cr7.models import GoatDetails

# Create your views here.

def who(request):
    details=GoatDetails.objects.all()
    data={'goat_details':details}
    return render(request,"cr7/goat.html",context=data)

def goat(request):
    goat_dict={"real_goat":"Ronaldo is the real GOAT"}
    return render(request,"cr7/cr7.html",context=goat_dict)
