from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.EmailInput, label='Email Address', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label='Password', max_length=25)