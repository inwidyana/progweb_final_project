from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views import View

import urllib.request
import json


class WeatherAPI(View):
    def get(self, request):
        url = 'https://api.darksky.net/forecast/b3c6d9e1b98483a7588e943e6c96eade/-7.7713847,110.3774998'
        serialized_data = urllib.request.urlopen(url).read()

        data = json.loads(serialized_data)
        data = data['hourly']
        # data = serializers.serialize('json', data)
        return JsonResponse(data)
