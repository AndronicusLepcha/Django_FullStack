from django import forms
from django.core import validators
from .models import UserData 

# class UserData(forms.Form):
#     firstname = forms.CharField(label='Enter your name', max_length=100)
#     email = forms.EmailField()

class NewUser(forms.ModelForm):
    class Meta(): 
        model=UserData
        fields = '__all__'




def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Needs to start with Z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    mail = forms.EmailField(label='Enter your email:')
    text = forms.CharField(widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        mail = all_clean_data['mail']

        if email != vmail:
            raise forms.ValidationError("Make sure to enter same email")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return botcatcher