from django.shortcuts import render
from basic_app.forms import UserForm,UserProfileInfoForm


from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context_dict={'text':'Hello World','number':100}
    return render(request,'basic_app/index.html',context=context_dict)
# def other(request):
#     return render(request,'basic_app/form.html')
@login_required
def special(request):
    return HttpResponse("You are logged in ,Nice !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    register = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password) #hashing the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            register = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request,'basic_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':register})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)


        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Accounts not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Passwod: {}".format(username,password))
            return HttpResponse("Invalid Login Details Supplied ")
    else:
        return render(request,'basic_app/login.html',{})

