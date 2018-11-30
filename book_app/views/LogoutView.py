from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth import logout


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login')