from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=250, help_text='eg. youremail@gmail.com', required=True)

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password1')


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50, required=True)
    name = forms.CharField(max_length=20, required=True)
    form_email = forms.EmailField(max_length=50, required=True)
    message = forms.CharField(
        max_length=500,
        widget=forms.Textarea(),
        help_text='Please include your message here.',
        required=True,
    )
