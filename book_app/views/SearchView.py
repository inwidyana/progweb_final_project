from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class SearchView(View):
    template = 'search.html'
    redirect_if_not_logged_in = '/'

    def get(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(self.redirect_if_not_logged_in)
        return render(request, self.template)
