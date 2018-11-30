from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    fname = forms.CharField(widget=forms.TextInput, label='First Name', max_length=50)
    lname = forms.CharField(widget=forms.TextInput, label='Last Name', max_length=50)
    username = forms.CharField(widget=forms.EmailInput, label='Email Address', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=25)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password', max_length=25)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        name = cleaned_data.get('name')
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Password does not match')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Email has been taken')