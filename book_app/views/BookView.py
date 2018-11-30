from django.shortcuts import render
from django.views import View

import urllib.request
import json


class BookView(View):
    template = 'book.html'

    def get(self, request):
        query = request.GET.get('q', '')
        url = 'https://www.googleapis.com/books/v1/volumes/' + query
        serialized_data = urllib.request.urlopen(url).read()

        data = json.loads(serialized_data)

        bookInfo = data["volumeInfo"]
        title = bookInfo["title"]
        authors = bookInfo["authors"]
        summary = bookInfo["description"]
        thumbnail = bookInfo['imageLinks']["thumbnail"]

        return render(request, self.template, {'title': title, 'authors': authors, 'summary': summary, 'thumbnail': thumbnail})
