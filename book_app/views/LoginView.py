from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from ..forms.LoginForm import LoginForm


class LoginView(View):
    form = LoginForm()
    template = 'auth/login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template, {'form': self.form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/login')

        return render(request, self.template, {'form': self.form})