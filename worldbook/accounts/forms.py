from django import forms
from allauth.account.forms import SignupForm
from django import forms as d_forms



class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='Ваше имя')
    last_name = forms.CharField(max_length=30, label='Ваша фамилия')



