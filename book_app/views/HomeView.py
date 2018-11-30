from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from ..forms.LoginForm import LoginForm


class HomeView(View):
    form = LoginForm()
    template = 'home.html'
    redirect_if_logged_in = '/home/'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.redirect_if_logged_in)
        return render(request, self.template, {'form': self.form})
