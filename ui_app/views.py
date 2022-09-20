# https://pypi.org/project/requests/
import requests
from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse, Http404
from json import loads

class ListRestaurantView(View):
    def get(self, request):
        url_restaurant = requests.get('http://127.0.0.1:8001/restaurants/')
        arr1 = []
        for i in loads(url_restaurant.text):
            arr1.append((i['name'], i['city']))
        print(arr1[0][0])
        ctx = {
            'restaurants': arr1,
        }
        return render(request, 'base.html', ctx)

class RestaurantDetailView(View):
    pass
