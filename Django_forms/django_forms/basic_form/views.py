from django.shortcuts import render
from . import forms
from basic_form.forms import NewUser
# Create your views here.

def form_name_view(request):
    # form = forms.FormName()

    # if request.method == 'POST':
    #     form=forms.FormName(request.POST)
    #     if form.is_valid():
    #         # do some thing here
    #         print("Validation success")
    #         print("Name: "+form.cleaned_data['name'])
    #         print("Email: "+form.cleaned_data['email'])
    #         print("Text: "+form.cleaned_data['text'])

    return render(request,'basic_forms/forms.html')



def UserLogin(request):
    user_data=NewUser()

    if request.method == "POST":
        form =NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return form_name_view(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'basic_forms/login.html',{'form':user_data})
