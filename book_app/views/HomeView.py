from django.views import View
from django.shortcuts import render

from ..forms.LoginForm import LoginForm


class HomeView(View):
    form = LoginForm()
    template = 'home.html'

    def get(self, request):
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect('/')
        return render(request, self.template, {'form': self.form})
