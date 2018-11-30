from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render


class IndexView(View):
    template = 'index.html'
    redirect_if_not_logged_in = '/'

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(self.redirect_if_not_logged_in)
        return render(request, self.template, {'fname': request.user.first_name, 'lname': request.user.last_name})
