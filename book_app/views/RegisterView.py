from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.contrib.auth.models import User

from ..forms.RegisterForm import RegisterForm


class RegisterView(View):
    form = RegisterForm()
    template = 'auth/login.html'
    redirect_after_successful_registration = '/home/'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.redirect_after_successful_registration)

        if request.GET.get('q', '') == 'register':
            return render(request, self.template, {'form': self.form, 'register': True})
        return render(request, self.template, {'form': self.form})

    def post(self, request):
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data.get('username'), form.cleaned_data.get('username'), form.cleaned_data.get('password'))
            user.first_name = form.cleaned_data.get('fname')
            user.last_name = form.cleaned_data.get('lname')
            user.save()

            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(self.redirect_after_successful_registration)

        return render(request, self.template, {'form': self.form, 'register': True})