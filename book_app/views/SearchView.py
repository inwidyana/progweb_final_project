from django.http import HttpResponse
from django.views import View

import urllib.request
import json


class SearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        url = 'https://www.googleapis.com/books/v1/volumes?q=' + query
        serialized_data = urllib.request.urlopen(url).read()

        data = json.loads(serialized_data)
        html = "<html><body><pre>Data: %s.</pre></body></html>" % json.dumps(data, indent=2)

        return HttpResponse(html)
