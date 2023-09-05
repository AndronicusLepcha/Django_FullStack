from django import forms

class Add_Goat(forms.Form):
    firstname = forms.CharField(label="Your First name", max_length=100)
    lastname = forms.CharField(label="Your Last name", max_length=100)
    message = forms.CharField(widget=forms.Textarea)