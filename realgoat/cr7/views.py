from django.shortcuts import render
from django.http import HttpResponse
from cr7.models import GoatDetails
from cr7.form import Add_Goat

# Create your views here.

def who(request):
    details=GoatDetails.objects.all()
    data={'goat_details':details}
    return render(request,"cr7/cr7.html",context=data)

def goat(request):
    details=GoatDetails.objects.all()
    data={'goat_details':details, 'real_goat':"Ronaldo is the real GOAT"}
    return render(request,"cr7/goat.html",context=data)


def Add(request):
    form=Add_Goat()
    details=GoatDetails.objects.all()
    data={'goat_details':details,'form':form}

    if request.method == 'POST':
        form = Add_Goat(request.POST)
        print("Hello")
        if form.is_valid():
            print("Validation Success")
            print("Name :"+form.cleaned_data['firstname'] +""+form.cleaned_data['lastname'])
            print("Message :"+form.cleaned_data['message'])

    return render(request,'cr7/goat.html',context=data)